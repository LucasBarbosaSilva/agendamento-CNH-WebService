<script lang="ts" setup>
	import type { Schedule } from '@/models/schedule';

	const props = defineProps<{
		schedule?: Schedule,
		loading?: boolean
	}>()

	const emit = defineEmits<{
		'close-click': [success: boolean]
	}>()
	
</script>

<template>
	<v-dialog width="400" :persistent="loading">
		<v-card v-if="!props.loading && props.schedule">
			<v-card-item class="bg-primary py-6">
				<template v-slot:prepend>
					<v-icon color="secondary" size="46">
						mdi-check-circle
					</v-icon>
				</template>
				<v-card-title class="text-h5 font-weight-bold">
					Agendamento realizado!
				</v-card-title>
			</v-card-item>
			<v-card-text>
				Seu agendamento do exame de vista para a CNH foi realizado com sucesso.
			</v-card-text>
			<v-card-text class="font-weight-bold text-blue-grey-darken-4">
				<v-row no-gutters class="mb-1">
					<v-icon color="indigo-darken-1" class="mr-2">
						mdi-calendar-month
					</v-icon>
					<p>{{ props.schedule?.data }}</p>
				</v-row>
				<v-row no-gutters>
					<v-icon color="indigo-darken-1" class="mr-2">
						mdi-clock
					</v-icon>
					<p>{{ props.schedule?.hora }}h</p>
				</v-row>
			</v-card-text>
			<v-card-actions class="justify-end px-3 pb-3">
				<v-btn
					color="indigo"	
					variant="elevated"	
					@click="emit('close-click', true)"
					class="px-10 font-weight-bold"
				>Ok</v-btn>
			</v-card-actions>
		
		</v-card>
		<v-card class="pb-6 text-center" v-else-if="props.loading">
			<v-card-title class="text-grey">
				Processando agendamento...
			</v-card-title>
			<v-card-text>
				<v-progress-circular
					color="primary"
					indeterminate
				/>
			</v-card-text>
		</v-card>
		<v-card class="pb-2" v-else>
			<v-card-item class="bg-error py-6">
				<template v-slot:prepend>
					<v-icon>
						mdi-message-alert
					</v-icon>
				</template>
				<v-card-title>
					Ocorreu um erro inesperado!
				</v-card-title>
			</v-card-item>
			<v-card-text class="text-blue-grey-darken-4">
				Não foi possível concluir o agendamento de seu exame
			</v-card-text>
			<v-card-actions class="justify-end">
				<v-btn
					color="pink-darken-4"	
					variant="elevated"	
					class="font-weight-bold"
					@click="emit('close-click', false)"
				>Fechar</v-btn>
			</v-card-actions>
		</v-card>
	</v-dialog>
</template>