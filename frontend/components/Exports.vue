<template>
  <div class="flex flex-row h-full justify-center lg:justify-end items-center content-center text-primary gap-4">
    <button @click="captureScreenshot" class="bg-secondary text-primary p-2 border-accent border-2 rounded-full hover:bg-accent hover:text-secondary active:bg-accent active:text-secondary transition ease-in-out duration-300" data-html2canvas-ignore="true">
      <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3.2" fill="currentColor"/><path fill="currentColor" d="M9 2L7.17 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2h-3.17L15 2H9zm3 15c-2.76 0-5-2.24-5-5s2.24-5 5-5s5 2.24 5 5s-2.24 5-5 5z"/></svg>
    </button>

    <button @click="exportData" class="bg-secondary text-primary p-2 border-accent border-2 rounded-full hover:bg-accent hover:text-secondary active:bg-accent active:text-secondary transition ease-in-out duration-300" data-html2canvas-ignore="true">
      <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" viewBox="0 0 24 24"><path fill="currentColor" d="M5 20h14v-2H5v2zM19 9h-4V3H9v6H5l7 7l7-7z"/></svg>    
    </button>
  </div>
</template>

<script>
import html2canvas from 'html2canvas';

export default {
  props: {
    data: Object,
  },
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
    },

    exportData() {
      console.log('Exporting data');
      
      // Download the data as json
      const jsonBlob = new Blob([JSON.stringify(this.data, null, 2)], {type: 'application/json'});
      const a = document.createElement('a');
      a.href = URL.createObjectURL(jsonBlob) 
      a.download = "your-discord-data.json";
      a.click();
    }
  }
}
</script>