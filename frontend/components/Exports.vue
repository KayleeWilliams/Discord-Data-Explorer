<template>
  <div class="flex flex-row h-full justify-end items-center content-center text-primary" data-html2canvas-ignore="true">
    <button @click="captureScreenshot" class="bg-secondary text-primary p-2 border-accent border-2 rounded-full hover:bg-accent hover:text-secondary active:bg-accent active:text-secondary transition ease-in-out duration-300 ">
      <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3.2" fill="currentColor"/><path fill="currentColor" d="M9 2L7.17 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2h-3.17L15 2H9zm3 15c-2.76 0-5-2.24-5-5s2.24-5 5-5s5 2.24 5 5s-2.24 5-5 5z"/></svg>
    </button>
  </div>
</template>

<script>
import html2canvas from 'html2canvas';

export default {
  methods: {
    captureScreenshot() {
      const options = {
        useCORS: true // Cors for cross origin images
      };

      html2canvas(document.body, options).then(canvas => {
        const a = document.createElement('a');
        a.href = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");
        a.download = 'your-discord-data.png';
        a.click();
      });
    }
  }
}
</script>