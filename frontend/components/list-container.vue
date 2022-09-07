<template>
    <div class = "flex flex-col gap-8 bg-secondary p-5 rounded-xl drop-shadow-lg">
        <p class="font-bold"> {{ title }} </p>
        <div class="text-left flex flex-row gap-4" v-for="(list, index) in list.slice(0, 5)" :key="index">
            <div class="bg-background text-primary h-12 w-12 flex justify-center items-center rounded-full">
                <p> {{ index + 1 }} </p>
            </div>
            <div>
                <p class="font-medium"> {{ list[1] }} </p>
                <p class="font-normal"> {{ list[2] }} Messages </p>
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