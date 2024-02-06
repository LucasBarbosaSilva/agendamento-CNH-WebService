<script lang="ts" setup>
	import { ref, computed } from 'vue';
	import { onClickOutside } from '@vueuse/core'

	const cardProps = defineProps<{
		timeText: string,
		active?: boolean,
		recentScheduled?: boolean
	}>()

	const emit = defineEmits(['time-scheduled'])

	const isSelected = ref(false)
	const cardRef = ref(null)
	onClickOutside(cardRef, event => isSelected.value = false)
	
	const locked = computed(() => cardProps.recentScheduled || !cardProps.active)

	const cardClass = computed(() => {
		if(cardProps.recentScheduled) {
			return 'bg-blue-darken-3 text-indigo-lighten-3'
		}else if (cardProps.active) {
			return 'bg-indigo'
		}else {
			return 'bg-indigo-lighten-2 text-indigo-lighten-4'
		}
	})

	function handleCardClick() {
		if (!locked.value){
			isSelected.value = true
		}
	}
</script>

<template>
	<v-hover>
		<template v-slot:default="{ isHovering, props }">
			<v-card
				ref="cardRef"
				v-bind="props"
				class="d-flex flex-column ma-3"
				:class="cardClass"
				:disabled="locked"
				:elevation="(!locked && isHovering) || isSelected ? 16 : 0"
				@click="handleCardClick()"
				rounded="lg"
				:width="150"
				:height="150"
			>
				<div class="flex-grow-1 d-flex flex-column align-center justify-center">
					<div v-if="cardProps.recentScheduled">
						<v-icon size="32" color="white" class="mt-n4">
							mdi-bookmark-check
						</v-icon>
					</div>

					<h4 class=" text-h4 font-weight-bold text-center">
						{{ cardProps.timeText }}
					</h4>

					<p v-if="cardProps.recentScheduled" class="text-indigo-lighten-5 text-caption">
						Agendado
					</p>
					<p v-else-if="!cardProps.active" class="mb-n6 text-caption">
						Indisponível
					</p>
				</div>

				<v-expand-transition>
					<div
						v-if="isSelected"
						class="d-flex flex-column align-center
						transition-fast-in-fast-out bg-indigo-darken-2 v-card--reveal w-100"
						style="height: 60%;"
					>
						<p class="font-weight-bold py-1 mb-1">Agendar ?</p>
						<span>
							<v-btn
								class="mr-1 font-weight-bold"
								variant="tonal"
								color="error"
								@click.stop="isSelected = false"
							>
								NÃO
							</v-btn>
							<v-btn
								class="font-weight-bold"
								variant="tonal"
								color="success"
								@click.stop="emit('time-scheduled')"
							>
								SIM
							</v-btn>
						</span>
					</div>
				</v-expand-transition>
			</v-card>
		</template>
	</v-hover>
</template>