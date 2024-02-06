<script setup lang="ts">
  import { ref, computed, onMounted } from 'vue';
  import DayContainer from '@/components/DayContainer.vue'
  import type { Schedule } from '@/models/schedule'
  import scheduleService from '@/services/scheduleService'
  
  const recentScheduleIds = ref<number[]>([1])
  const schedules = ref<Schedule[]>([])
  const loading = ref(false)

  const schedulesByDate = computed(() => {
    const groups = schedules.value.reduce((group: {[key: string]: Schedule[]}, item) => {
    if (!group[item.data]) {
      group[item.data] = []
    }
    group[item.data].push(item)
    return group
    }, {})

    const entries: [string, Schedule[]][] = Object.entries(groups)
    entries.sort((a, b) => new Date(a[0]).getTime() - new Date(b[0]).getTime())

    return entries
  })

  async function fetchSchedules() {
    loading.value = true
    try {
      const res = await scheduleService.get()
      schedules.value = res.data
    } catch (error) {
      console.error(error)
    }
    loading.value = false
  }

  onMounted(() => {
    fetchSchedules()
  })
</script>

<template>
  <main>
    <DayContainer
      v-if="!loading && schedulesByDate.length > 0"
      v-for="[day, schedules] in schedulesByDate"
      :day="day"
      :schedules="schedules"
      :recent-schedule-ids="recentScheduleIds"
      @schedule-updated="fetchSchedules"
    />
    <div class="w-100 text-center" v-else-if="loading">
      <v-progress-circular
        color="primary"
        indeterminate
      />
    </div>
    <p class="font-weight-bold text-blue-grey-darken-3" v-else>
      Dados de agendamento não disponíveis
    </p>
  </main>
</template>
