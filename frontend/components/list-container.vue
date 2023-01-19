<template>
    <div class = "flex flex-col gap-8 bg-secondary p-4 rounded-xl drop-shadow-lg w-full">
        <h3 class="font-bold"> {{ title }} </h3>
        <div class="text-left flex flex-row gap-4 h-12" v-for="(list, index) in list.slice(0, 5)" :key="index">
            <div class="bg-background text-primary flex justify-center items-center rounded-full shrink-0 w-12">
                <img v-if="!list.error" :src="`https://cdn.discordapp.com/avatars/${list.id}/${list.avatar}`" class="w-full h-full rounded-full" @error="list.error = true" />
                <p v-if="list.error"> {{ index + 1 }} </p>
                <!-- how do you do python equivilant of f-string in vuejs/nuxt -->

            </div>
            <div class="truncate">
                <p class="font-medium inline"> {{ list.name }} </p>
                <p class="font-normal block"> {{ list.messages }} Messages </p>
            </div>
        </div>
    </div>
</template>

<script> 
export default {
  props: {
    title: String,
    list: Array,
  }
}
</script>