<template>
  <div class="flex flex-col items-center justify-between content-center h-screen bg-background">

    <!-- Meta Tags -->
    <Head>
      <Title>Discord Data Explorer</Title>
      <Meta name="viewport" content="width=device-width initial-scale=1.0"/> 
    </Head>

    <div />

    <div v-if="hasUploaded">
      <ResultsView :data="data" />
    </div>

    <div v-else>
      <UploadView @uploadSuccess="fileUploaded"/>
    </div>

    <footer class="py-4 bg-background w-full">
      <p class="text-center text-gray-500 text-xs">
        Created by Kaylee Williams, Available on 
        <a class="underline underline-offset-2 hover:text-[#4465F1] transition duration-300 ease-in-out" href="https://github.com/KayleeWilliams/Discord-Data-Explorer" target="_blank">
          Github</a>.
      </p>
    </footer>
  </div>
</template>

<script setup>
  let hasUploaded = ref(false);
  let data = ref([]);

  function fileUploaded(res) {
    data.value = res;
    hasUploaded.value = true;
  }
</script>