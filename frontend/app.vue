<template>
  <div class="">

    <!-- Meta Tags -->
    <Head>
      <Title>Discord Data Explorer</Title>
      <Meta name="viewport" content="width=device-width initial-scale=1.0"/> 
    </Head>

    <div v-if="hasUploaded">
      <p> Uploaded </p>
    </div>

    <div v-else>
      <upload-section />
    </div>
  </div>
</template>

