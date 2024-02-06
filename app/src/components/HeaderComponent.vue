<template>
  <v-app-bar>
    <template v-slot:prepend>
      <v-icon :size="36" color="primary" class="ml-4">
        mdi-eye-circle
      </v-icon>
    </template>

    <v-app-bar-title
      class="font-weight-bold text-blue-grey-darken-4"
    > Exame de Vista </v-app-bar-title>

    <template v-slot:append>
      <p class="text-blue-grey-darken-1 mr-4">Agendamento para CNH</p>
    </template>
  </v-app-bar>	
</template>