<template>
    <div class = "flex flex-col gap-8 bg-secondary p-4 rounded-xl drop-shadow-lg w-full">
        <div class="flex flex-row justify-between items-center">
        <div class="w-10 h-10" />
        <h3 class="font-bold"> {{ title }} </h3>

        <button
            v-show="toggle"
            type="button"
            class="relative inline-flex items-center px-2 py-2 bg-background focus:z-10 active:bg-gray-100 transition ease-in-out duration-150 rounded-full float-right"
            @click="$emit('messageToggle')">
          <svg class="text-secondary w-6 h-6" viewBox="0 0 24 24"><path fill="currentColor" d="M2 17h2v.5H3v1h1v.5H2v1h3v-4H2v1zm1-9h1V4H2v1h1v3zm-1 3h1.8L2 13.1v.9h3v-1H3.2L5 10.9V10H2v1zm5-6v2h14V5H7zm0 14h14v-2H7v2zm0-6h14v-2H7v2z"></path></svg>
        </button>

        <div class="w-10 h-10" v-if="!toggle" />

        </div>

        <!-- Loop through each friend -->
        <div class="text-left flex flex-row gap-4 h-12" v-for="(list, index) in list.slice(0, 5)" :key="index">
            <div class="bg-background text-primary flex justify-center items-center rounded-full shrink-0 w-12">
                <img v-if="!list.error" :src="`https://cdn.discordapp.com/avatars/${list[0]}/${list[1]['avatar']}`" class="w-full h-full rounded-full" @error="list.error = true" />
                <p v-if="list.error"> {{ index + 1 }} </p>
            </div>
            <div class="truncate">
                <p class="font-medium inline"> {{ list[1]["name"] }} </p>
                <p class="font-normal block"> {{ list[1]["messages"]}} Messages </p>
            </div>
        </div>
    </div>
</template>

<script> 
export default {
  props: {
    title: String,
    list: Array,
    toggle: Boolean
  }
}
</script>