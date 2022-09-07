<template>
  <div class="">

    <!-- Meta Tags -->
    <Head>
      <Title>Discord Data Explorer</Title>
      <Meta name="viewport" content="width=device-width initial-scale=1.0"/> 
    </Head>

    <div v-if="hasUploaded">
      <result-section :data="data" />
    </div>

    <div v-else>
      <upload-section @uploadSuccess="fileUploaded"/>
    </div>
  </div>
</template>

<script setup>
  let hasUploaded = ref(false);
  let data = ref([]);

  function fileUploaded(res) {
    data.value = res;
    console.log(res);
    hasUploaded.value = true;
  }
</script>