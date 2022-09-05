<template>
    <div class="bg-background text-primary flex flex-col text-center justify-center content-center gap-8 h-screen w-full">
        <p class="text-2xl sm:text-4xl lg:text-6xl font-bold drop-shadow-lg"> Discord Data Package Explorer </p>
        <p class="text-lg sm:text-2xl lg:text-3xl font-normal drop-shadow-lg"> Upload your data package to get started. </p>

        <div class="flex flex-row justify-center content-center drop-shadow-lg mt-4">
            <input type="file" accept=".zip" id="files" @change="handleFile($event)" hidden />
            <label for="files"
                class="bg-primary text-background hover:opacity-90 select-none text-lg px-6 py-4 rounded-l-lg drop-shadow-lg transition ease-in-out delay-150 duration-150 hover:-translate-y-1 hover:scale-105"> Select File
            </label>

            <button v-on:click="submitFile"
                    class="flex flex-row text-primary bg-secondary hover:opacity-90 select-none text-lg px-6 py-4 rounded-r-lg drop-shadow-lg transition ease-in-out delay-150 duration-150 hover:-translate-y-1 hover:scale-105"> 
                    <div>
                        <div v-show="isLoading == true" class="rounded-full border-violet-100 border-t-violet-100/0 w-6 h-6 border-4 border-solid animate-spin mr-2"></div>
                    </div>
                    Submit
                </button>
        </div>
    </div>
</template>

<script setup>
    let file = '';
    let loading = false;
    const emit = defineEmits(['uploadSuccess'])

    const handleFile = (event) => {
        file = event.target.files[0];
    }

    async function submitFile(){
        loading = true;

        let formData = new FormData();
        formData.append('file', file);

        let res = await fetch( 'http://localhost:3001/uploader', {
            method: 'POST',
            body: formData
            
        } );

        console.log(res.data); 
        emit('uploadSuccess', res.data)
    }
</script>