<script lang="ts" setup>
	import { ref } from 'vue';
	import TimeCard from '@/components/TimeCard.vue'
	import SuccessDialog from './SuccessDialog.vue';
	import type { Schedule } from '@/models/schedule'
	import scheduleService from '@/services/scheduleService';
	
	const props = defineProps<{
		day: string,
		schedules: Schedule[],
		recentScheduleIds: number[]
	}>()

	const emit = defineEmits(['schedule-updated'])

	const loadingSchedule = ref(false)
	const showDialog = ref(false)
	const scheduled = ref<Schedule>()

	async function updateSchedule(s: Schedule) {
		if(!s) return
		
		loadingSchedule.value = true
		try {
			showDialog.value = true
			await scheduleService.update(s)
			scheduled.value = s
		} catch (error) {
			console.error(error)
		}
		loadingSchedule.value = false
	}

	function handleDialogClose(success: boolean) {
		showDialog.value = false
		if(success) emit('schedule-updated')
	}
</script>

<template>
	<h2 class="text-primary mb-4">Dia {{ props.day }}</h2>
	<v-row
		class="bg-blue-grey-lighten-5 pa-2 rounded-lg"
		no-gutters
	>
		<TimeCard
			v-for="s in props.schedules"
			:key="s.id"
			:time-text="`${s.hora}h`"
			:active="!s.agendado"
			:recent-scheduled="props.recentScheduleIds.includes(s.id)"
			@time-scheduled="updateSchedule(s)"
		/>
	</v-row>

	<v-divider class="my-8" />

	<SuccessDialog
		v-model="showDialog"
		:schedule="scheduled"
		:loading="loadingSchedule"
		@close-click="handleDialogClose"
	/>
</template>