<template>
    <div class="bg-background text-primary flex flex-col text-center justify-center content-center items-center gap-8 w-full h-full">
        <p class="text-2xl sm:text-4xl lg:text-6xl font-bold drop-shadow-lg"> Discord Data Package Explorer </p>
        <p class="text-lg sm:text-2xl lg:text-3xl font-normal drop-shadow-lg"> Upload your data package to get started. </p>

        <div class="bg-gradient-to-br from-accent via-[#D953D2] to-[#FF5B9F] p-1 rounded-lg"> 
            <div class="flex flex-row bg-secondary text-primary w-full h-full select-none items-center text-lg gap-2 rounded-lg">
                <input type="file" accept=".zip" id="files" @change="handleFile($event)" hidden />
                <label for="files"
                    class="px-4 py-4 font-medium tracking-wide hover:text-accent rounded-lg"> Select File
                </label>

                <button v-on:click="submitFile"
                    class="flex flex-row bg-accent hover:bg-primary rounded-full items-center justify-center p-2 mr-4 group transistion ease-in-out duration-150 delay-75"> 
                    <svg v-show="isLoading == false" class="w-6 h-6 text-primary group-hover:text-accent" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="M9 16h6v-6h4l-7-7l-7 7h4zm-4 2h14v2H5z"/></svg>
                    <div v-show="isLoading == true" class="rounded-full border-primary group-hover:border-accent group-hover:border-t-black/0 group-hover:animate-spin border-t-black/0 w-6 h-6 border-4 border-solid animate-spin" />
                </button>
            </div>
        </div>

    </div>
</template>

<script setup>
    let file = '';
    let isLoading = ref(false);
    const emit = defineEmits(['uploadSuccess']);

    const handleFile = (event) => {
        file = event.target.files[0];
    }

    async function submitFile(){
        isLoading.value = true;

        let formData = new FormData();
        formData.append('file', file);


        let res = await fetch( 'http://127.0.0.1:3001/uploader', {
            method: 'POST',
            body: formData
            });

        if (res.status == 200) {
            let data = await res.json();
            emit('uploadSuccess', data)
        }
    }
</script>