<template>
    <div class = "flex flex-col gap-8 bg-secondary p-4 rounded-xl drop-shadow-lg w-full">
        <p class="font-bold"> {{ title }} </p>
        <div class="text-left flex flex-row gap-4 h-12" v-for="(list, index) in list.slice(0, 5)" :key="index">
            <div class="bg-background text-primary flex justify-center items-center rounded-full shrink-0 w-12">
                <p> {{ index + 1 }} </p>
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