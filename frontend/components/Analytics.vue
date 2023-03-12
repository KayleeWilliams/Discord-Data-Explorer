<template>
  <div class="w-full bg-secondary py-4 pl-2 drop-shadow-lg rounded-xl flex justify-center">
    <div class="w-11/12 text-start grid grid-cols-1 lg:grid-cols-2 grid-rows-auto gap-2">
      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M14 19h4V5h-4M6 19h4V5H6v14Z"/></svg>
        <p class="text-primary"> Discord paused Spotify <span class="font-bold text-accent"> {{ data["spotify_auto_paused"] }} </span> times </p>
      </div>
      
      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M17.9 10.9C14.7 9 9.35 8.8 6.3 9.75c-.5.15-1-.15-1.15-.6c-.15-.5.15-1 .6-1.15c3.55-1.05 9.4-.85 13.1 1.35c.45.25.6.85.35 1.3c-.25.35-.85.5-1.3.25m-.1 2.8c-.25.35-.7.5-1.05.25c-2.7-1.65-6.8-2.15-9.95-1.15c-.4.1-.85-.1-.95-.5c-.1-.4.1-.85.5-.95c3.65-1.1 8.15-.55 11.25 1.35c.3.15.45.65.2 1m-1.2 2.75c-.2.3-.55.4-.85.2c-2.35-1.45-5.3-1.75-8.8-.95c-.35.1-.65-.15-.75-.45c-.1-.35.15-.65.45-.75c3.8-.85 7.1-.5 9.7 1.1c.35.15.4.55.25.85M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10a10 10 0 0 0 10-10A10 10 0 0 0 12 2Z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["spotify_listen_along_started"] }} </span> Listen alongs </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M12 5.5A3.5 3.5 0 0 1 15.5 9a3.5 3.5 0 0 1-3.5 3.5A3.5 3.5 0 0 1 8.5 9A3.5 3.5 0 0 1 12 5.5M5 8c.56 0 1.08.15 1.53.42c-.15 1.43.27 2.85 1.13 3.96C7.16 13.34 6.16 14 5 14a3 3 0 0 1-3-3a3 3 0 0 1 3-3m14 0a3 3 0 0 1 3 3a3 3 0 0 1-3 3c-1.16 0-2.16-.66-2.66-1.62a5.536 5.536 0 0 0 1.13-3.96c.45-.27.97-.42 1.53-.42M5.5 18.25c0-2.07 2.91-3.75 6.5-3.75s6.5 1.68 6.5 3.75V20h-13v-1.75M0 20v-1.5c0-1.39 1.89-2.56 4.45-2.9c-.59.68-.95 1.62-.95 2.65V20H0m24 0h-3.5v-1.75c0-1.03-.36-1.97-.95-2.65c2.56.34 4.45 1.51 4.45 2.9V20Z"/></svg>
        <p class="text-primary">  <span class="font-bold text-accent"> {{ data["guild_joined"] }} </span> Servers joined </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8"  viewBox="0 0 24 24"><path fill="currentColor" d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5l-1.5 1.5l-5-5v-.79l-.27-.27A6.516 6.516 0 0 1 9.5 16A6.5 6.5 0 0 1 3 9.5A6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14S14 12 14 9.5S12 5 9.5 5Z"/></svg>
        <p class="text-primary">  <span class="font-bold text-accent"> {{ data["guild_viewed"] }} </span> Servers viewed </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M13.34 8.17c-.93 0-1.69-.77-1.69-1.7a1.69 1.69 0 0 1 1.69-1.69c.94 0 1.7.76 1.7 1.69c0 .93-.76 1.7-1.7 1.7M10.3 19.93l-5.93-1.18l.34-1.7l4.15.85l1.35-6.86l-1.52.6v2.86H7v-3.96l4.4-1.87l.67-.08c.6 0 1.1.34 1.43.85l.86 1.35c.68 1.21 2.03 2.03 3.64 2.03v1.68c-1.86 0-3.56-.83-4.66-2.1l-.5 2.54l1.77 1.69V23h-1.69v-5.1l-1.78-1.69l-.84 3.72M21 23h-2V3H6v13.11l-2-.42V1h17v22M6 23H4v-3.22l2 .42V23Z"/></svg>
        <p class="text-primary">  <span class="font-bold text-accent"> {{ data["leave_guild"] }} </span> Servers left </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2L9.19 8.63L2 9.24l5.46 4.73L5.82 21z"/></svg>
        <p class="text-primary">  <span class="font-bold text-accent"> {{ data["gif_favorited"] }} </span> Gifs favourited </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="m22 9.24l-7.19-.62L12 2L9.19 8.63L2 9.24l5.46 4.73L5.82 21L12 17.27L18.18 21l-1.63-7.03L22 9.24zM12 15.4l-3.76 2.27l1-4.28l-3.32-2.88l4.38-.38L12 6.1l1.71 4.04l4.38.38l-3.32 2.88l1 4.28L12 15.4z"/></svg> 
        <p class="text-primary">  <span class="font-bold text-accent"> {{ data["gif_unfavorited"] }} </span> Gifs unfavourited </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5l-8-5V6l8 5l8-5v2z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["create_instant_invite"] }} </span> Invites created </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M20 6h-8l-2-2H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-1 8h-3v3h-2v-3h-3v-2h3V9h2v3h3v2z"/></svg>
        <p class="text-primary">  <span class="font-bold text-accent"> {{ data["create_channel"] }} </span> Channels created </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM8.5 8c.83 0 1.5.67 1.5 1.5S9.33 11 8.5 11S7 10.33 7 9.5S7.67 8 8.5 8zM12 18c-2.28 0-4.22-1.66-5-4h10c-.78 2.34-2.72 4-5 4zm3.5-7c-.83 0-1.5-.67-1.5-1.5S14.67 8 15.5 8s1.5.67 1.5 1.5s-.67 1.5-1.5 1.5z"/></svg>
        <p class="text-primary">  <span class="font-bold text-accent"> {{ data["create_emoji"] }} </span> Emojis created </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M21 2H3c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2m0 18H3V6h18v14Z"/></svg>
        <p class="text-primary">  <span class="font-bold text-accent"> {{ data["application_created"] }} </span> Applications created </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="m20 22l-3.86-1.55c.7-1.53 1.2-3.11 1.51-4.72L20 22M7.86 20.45L4 22l2.35-6.27c.31 1.61.81 3.19 1.51 4.72M12 2s5 2 5 10c0 3.1-.75 5.75-1.67 7.83A2 2 0 0 1 13.5 21h-3a2 2 0 0 1-1.83-1.17C7.76 17.75 7 15.1 7 12c0-8 5-10 5-10m0 10c1.1 0 2-.9 2-2s-.9-2-2-2s-2 .9-2 2s.9 2 2 2Z"/></svg>
        <p class="text-primary">  <span class="font-bold text-accent"> {{ data["premium_guild_subscription_created"] }} </span> Server boosts </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M12 0L8 4h2v4h4V4h2M1 2v2h2l3.6 7.6L5.2 14c-.1.3-.2.6-.2 1c0 1.1.9 2 2 2h12v-2H7.4c-.1 0-.2-.1-.2-.2v-.1l.9-1.7h7.4c.7 0 1.4-.4 1.7-1l3.9-7l-1.7-1l-3.9 7h-7L4.3 2M7 18c-1.1 0-2 .9-2 2s.9 2 2 2s2-.9 2-2s-.9-2-2-2m10 0c-1.1 0-2 .9-2 2s.9 2 2 2s2-.9 2-2s-.9-2-2-2Z"/></svg>
        <p class="text-primary">  <span class="font-bold text-accent"> {{ data["premium_upsell_viewed"] }} </span> Times you was upsold </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M21 19v1H3v-1l2-2v-6c0-3.1 2.03-5.83 5-6.71V4a2 2 0 0 1 2-2a2 2 0 0 1 2 2v.29c2.97.88 5 3.61 5 6.71v6l2 2m-7 2a2 2 0 0 1-2 2a2 2 0 0 1-2-2"/></svg>
        <p class="text-primary">  <span class="font-bold text-accent"> {{ data["notification_clicked"] }} </span> Notifications clicked </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M19 4H5a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h4v-2H5V8h14v10h-4v2h4c1.1 0 2-.9 2-2V6a2 2 0 0 0-2-2zm-7 6l-4 4h3v6h2v-6h3l-4-4z"/></svg>
        <p class="text-primary"> Discord opened <span class="font-bold text-accent"> {{ data["app_opened"] }} </span> times </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M18 1c-2.76 0-5 2.24-5 5s2.24 5 5 5s5-2.24 5-5s-2.24-5-5-5zm.5 6h-1V3h1v4zm0 1v1h-1V8h1zm-.59 5c.06.16.09.33.09.5c0 .83-.67 1.5-1.5 1.5s-1.5-.67-1.5-1.5c0-.39.15-.74.39-1.01A7.032 7.032 0 0 1 11.68 9H5.81l1.04-3H11c0-.69.1-1.37.29-2H6.5c-.66 0-1.21.42-1.42 1.01L3 11v8c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-1h12v1c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-6.68c-1.05.51-2.16.69-3.09.68zM7.5 15c-.83 0-1.5-.67-1.5-1.5S6.67 12 7.5 12s1.5.67 1.5 1.5S8.33 15 7.5 15z"/></svg>
        <p class="text-primary"> Discord crashed <span class="font-bold text-accent"> {{ data["app_crashed"] }} </span> times </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M4 8h4V4H4v4zm6 12h4v-4h-4v4zm-6 0h4v-4H4v4zm0-6h4v-4H4v4zm6 0h4v-4h-4v4zm6 6h4v-4h-4v4zm3-20c-2.76 0-5 2.24-5 5s2.24 5 5 5s5-2.24 5-5s-2.24-5-5-5zm.5 8h-1V7h1v1zm0-2h-1V2h1v4zM16 14h4v-2.07c-.33.05-.66.07-1 .07c-1.07 0-2.09-.24-3-.68V14zM10 4v4h2.68c-.44-.91-.68-1.93-.68-3c0-.34.02-.67.07-1H10z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["guild_outage_viewed"] }} </span> Server outages experienced </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M18 15c0 2.6-1.2 4.9-3.1 6.3l-.5-.5l-2.1-2.1l1.4-1.4l1.2 1.2c.5-.7.9-1.6 1-2.5H14v-2h1.9c-.2-.9-.5-1.7-1-2.5l-1.2 1.2l-1.4-1.4l1.2-1.2c-.7-.5-1.6-.9-2.5-1V11H9V9.1c-.9.2-1.7.5-2.5 1l3 3c.2 0 .3-.1.5-.1a2 2 0 1 1 0 4c-1.11 0-2-.89-2-2c0-.2 0-.3.1-.5l-3-3c-.5.7-.9 1.6-1 2.5H6v2H4.1c.2.9.5 1.7 1 2.5l1.2-1.2l1.4 1.4l-2.6 2.6C3.2 19.9 2 17.6 2 15c0-4.42 3.58-8 8-8s8 3.58 8 8m5-10c0-1.66-1.34-3-3-3s-3 1.34-3 3c0 1.3.84 2.4 2 2.82V11h2V7.82C22.16 7.4 23 6.3 23 5m-3 1c-.55 0-1-.45-1-1s.45-1 1-1s1 .45 1 1s-.45 1-1 1Z"/></svg>
        <p class="text-primary"> Hit the server limit <span class="font-bold text-accent"> {{ data["guild_limit_reached"] }} </span> times </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M19 3H5c-1.11 0-2 .89-2 2v4h2V5h14v14H5v-4H3v4a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2m-8.92 12.58L11.5 17l5-5l-5-5l-1.42 1.41L12.67 11H3v2h9.67l-2.59 2.58Z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["login_successful"] }} </span> Logins </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M10.18 17H7v-2h3c.08-.68.23-1.36.5-2H7v-2h4.82c.03-.03.05-.06.08-.1A6.53 6.53 0 0 1 16.5 9H7V7h10v2h-.5c1.62 0 3.24.61 4.5 1.82V5a2 2 0 0 0-2-2h-4.18C14.4 1.84 13.3 1 12 1s-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14a2 2 0 0 0 2 2h8.06c-.41-.26-.8-.55-1.16-.9c-.9-.89-1.45-1.97-1.72-3.1M12 3c.55 0 1 .45 1 1s-.45 1-1 1s-1-.45-1-1s.45-1 1-1m8.31 14.9c.44-.69.69-1.52.69-2.4c0-2.5-2-4.5-4.5-4.5S12 13 12 15.5s2 4.5 4.5 4.5c.87 0 1.69-.25 2.38-.68L22 22.39L23.39 21l-3.08-3.1m-3.81.1a2.5 2.5 0 0 1 0-5a2.5 2.5 0 0 1 0 5Z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["search_started"] }} </span> Searches </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M16 9V4h1c.55 0 1-.45 1-1s-.45-1-1-1H7c-.55 0-1 .45-1 1s.45 1 1 1h1v5c0 1.66-1.34 3-3 3v2h5.97v7l1 1l1-1v-7H19v-2c-1.66 0-3-1.34-3-3z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["search_started"] }} </span> Messages pinned </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M9 16h6v-6h4l-7-7l-7 7h4zm-4 2h14v2H5z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["upload_drag_and_drop_count"] }} </span> Files dragged & dropped </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M18 9V7h-2V2.84A9.929 9.929 0 0 0 11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12c0-1.05-.17-2.05-.47-3H18zm-2.5-1c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5s-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5zm-7 0c.83 0 1.5.67 1.5 1.5S9.33 11 8.5 11S7 10.33 7 9.5S7.67 8 8.5 8zm3.5 9.5c-2.33 0-4.31-1.46-5.11-3.5h10.22c-.8 2.04-2.78 3.5-5.11 3.5zM22 3h2v2h-2v2h-2V5h-2V3h2V1h2v2z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["add_reaction"] }} </span> Reactions added </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M12 12Zm0 10q-2.075 0-3.9-.788q-1.825-.787-3.175-2.137q-1.35-1.35-2.137-3.175Q2 14.075 2 12t.788-3.9q.787-1.825 2.137-3.175q1.35-1.35 3.175-2.138Q9.925 2 12 2q1.075 0 2.075.212q1 .213 1.925.613v2.25q-.875-.5-1.887-.788Q13.1 4 12 4Q8.675 4 6.338 6.337Q4 8.675 4 12t2.338 5.663Q8.675 20 12 20q3.325 0 5.663-2.337Q20 15.325 20 12q0-.8-.163-1.55Q19.675 9.7 19.4 9h2.15q.225.725.338 1.462Q22 11.2 22 12q0 2.075-.788 3.9q-.787 1.825-2.137 3.175q-1.35 1.35-3.175 2.137Q14.075 22 12 22Zm8-15V5h-2V3h2V1h2v2h2v2h-2v2Zm-4.5 4q.625 0 1.062-.438Q17 10.125 17 9.5t-.438-1.062Q16.125 8 15.5 8t-1.062.438Q14 8.875 14 9.5t.438 1.062Q14.875 11 15.5 11Zm-7 0q.625 0 1.062-.438Q10 10.125 10 9.5t-.438-1.062Q9.125 8 8.5 8t-1.062.438Q7 8.875 7 9.5t.438 1.062Q7.875 11 8.5 11Zm3.5 6.5q1.7 0 3.088-.962Q16.475 15.575 17.1 14H6.9q.625 1.575 2.013 2.538Q10.3 17.5 12 17.5Z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["remove_reaction"] }} </span> Reactions removed</p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="m22.7 14.3l-1 1l-2-2l1-1c.1-.1.2-.2.4-.2c.1 0 .3.1.4.2l1.3 1.3c.1.2.1.5-.1.7M13 19.9V22h2.1l6.1-6.1l-2-2l-6.2 6M21 5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h6v-1.9l1.1-1.1H5l3.5-4.5l2.5 3l3.5-4.5l1.6 2.1l4.9-5V5Z"/></svg>
        <p class="text-primary"> Profile picture updated <span class="font-bold text-accent"> {{ data["user_avatar_updated"] }} </span> times </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M16 12a2 2 0 0 1 2-2a2 2 0 0 1 2 2a2 2 0 0 1-2 2a2 2 0 0 1-2-2m-6 0a2 2 0 0 1 2-2a2 2 0 0 1 2 2a2 2 0 0 1-2 2a2 2 0 0 1-2-2m-6 0a2 2 0 0 1 2-2a2 2 0 0 1 2 2a2 2 0 0 1-2 2a2 2 0 0 1-2-2Z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["user_avatar_updated"] }} </span> Status updates </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M20 12c0-1.1.9-2 2-2V6c0-1.1-.9-2-2-2H4c-1.1 0-1.99.9-1.99 2v4c1.1 0 1.99.9 1.99 2s-.89 2-2 2v4c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2v-4c-1.1 0-2-.9-2-2zm-4.42 4.8L12 14.5l-3.58 2.3l1.08-4.12l-3.29-2.69l4.24-.25L12 5.8l1.54 3.95l4.24.25l-3.29 2.69l1.09 4.11z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["user_avatar_updated"] }} </span> Activity updates </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M21 7L9 19l-5.5-5.5l1.41-1.41L9 16.17L19.59 5.59L21 7Z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["captcha_solved"] }} </span> Captchas solved </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a.996.996 0 0 0 0-1.41l-2.34-2.34a.996.996 0 0 0-1.41 0l-1.83 1.83l3.75 3.75l1.83-1.83z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["message_edited"] }} </span> Messages edited </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["message_deleted"] }} </span> Messages deleted </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M20 15.5c-1.25 0-2.45-.2-3.57-.57a1.02 1.02 0 0 0-1.02.24l-2.2 2.2a15.045 15.045 0 0 1-6.59-6.59l2.2-2.21a.96.96 0 0 0 .25-1A11.36 11.36 0 0 1 8.5 4c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1c0 9.39 7.61 17 17 17c.55 0 1-.45 1-1v-3.5c0-.55-.45-1-1-1zM19 12h2a9 9 0 0 0-9-9v2c3.87 0 7 3.13 7 7zm-4 0h2c0-2.76-2.24-5-5-5v2c1.66 0 3 1.34 3 3z"/></svg>
        <p class="text-primary"> Started speaking <span class="font-bold text-accent"> {{ data["start_speaking"] }} </span> times </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M17 20c-.29 0-.56-.06-.76-.15c-.71-.37-1.21-.88-1.71-2.38c-.51-1.56-1.47-2.29-2.39-3c-.79-.61-1.61-1.24-2.32-2.53C9.29 10.98 9 9.93 9 9c0-2.8 2.2-5 5-5s5 2.2 5 5h2c0-3.93-3.07-7-7-7S7 5.07 7 9c0 1.26.38 2.65 1.07 3.9c.91 1.65 1.98 2.48 2.85 3.15c.81.62 1.39 1.07 1.71 2.05c.6 1.82 1.37 2.84 2.73 3.55A3.999 3.999 0 0 0 21 18h-2c0 1.1-.9 2-2 2zM7.64 2.64L6.22 1.22C4.23 3.21 3 5.96 3 9s1.23 5.79 3.22 7.78l1.41-1.41C6.01 13.74 5 11.49 5 9s1.01-4.74 2.64-6.36zM11.5 9a2.5 2.5 0 0 0 5 0a2.5 2.5 0 0 0-5 0z"/></svg>
        <p class="text-primary"> Started listening <span class="font-bold text-accent"> {{ data["start_listening"] }} </span> times </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M12 14c1.66 0 2.99-1.34 2.99-3L15 5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3zm5.3-3c0 3-2.54 5.1-5.3 5.1S6.7 14 6.7 11H5c0 3.41 2.72 6.23 6 6.72V21h2v-3.28c3.28-.48 6-3.3 6-6.72h-1.7z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["mic_testing_started"] }} </span> Mic tests </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M20 18c1.1 0 1.99-.9 1.99-2L22 6a2 2 0 0 0-2-2H4c-1.11 0-2 .89-2 2v10a2 2 0 0 0 2 2H0v2h24v-2h-4zM4 16V6h16v10.01L4 16zm9-6.87c-3.89.54-5.44 3.2-6 5.87c1.39-1.87 3.22-2.72 6-2.72v2.19l4-3.74L13 7v2.13z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["screenshare_finished"] }} </span> Screenshares </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="m21 11l-6-6v5H8c-2.76 0-5 2.24-5 5v4h2v-4c0-1.65 1.35-3 3-3h7v5l6-6z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["keyboard_shortcut_used"] }} </span> Keyboard shortcuts </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M21 4v4.12L19.12 10H4.76L3 6.47V18h8v2H3a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1l2 4h3L7 4h2l2 4h3l-2-4h2l2 4h3l-2-4h4m.42 8.3l1.28 1.28c.22.21.22.56 0 .77l-1 1l-2.05-2.05l1-1c.11-.11.25-.17.39-.17s.27.06.38.17m-.3 3.63L15.06 22H13v-2.06l6.07-6.06l2.05 2.05Z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["streamer_mode_toggle"] }} </span> Streamer mode toggles </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M24 9v2h-6V9h6zM8 4C5.79 4 4 5.79 4 8s1.79 4 4 4s4-1.79 4-4s-1.79-4-4-4zm0 9c-2.67 0-8 1.34-8 4v3h16v-3c0-2.66-5.33-4-8-4zm4.51-8.95C13.43 5.11 14 6.49 14 8s-.57 2.89-1.49 3.95C14.47 11.7 16 10.04 16 8s-1.53-3.7-3.49-3.95zm4.02 9.78C17.42 14.66 18 15.7 18 17v3h2v-3c0-1.45-1.59-2.51-3.47-3.17z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["remove_channel_recipient"] }} </span> Users removed from group </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M13 2v5.08A5.47 5.47 0 0 0 12 7a5.47 5.47 0 0 0-1 .08V2m5.9 13a5 5 0 0 1-.17.55L20 17.42V22h-2v-3.42l-2.26-1.29a4.94 4.94 0 0 1-7.48 0L6 18.58V22H4v-4.58l3.27-1.87A5 5 0 0 1 7.1 15H5.3l-2.75 1.83l-1.1-1.66L4.7 13h2.4a5 5 0 0 1 .27-.88l-1.56-1l-3.57.88l-.48-2l4.43-1.08l2.31 1.53a5 5 0 0 1 7 0l2.27-1.53L22.24 10l-.48 2l-3.57-.89l-1.56 1a5 5 0 0 1 .27.89h2.4l3.25 2.16l-1.1 1.66L18.7 15M11 14a1 1 0 1 0-1 1a1 1 0 0 0 1-1m4 0a1 1 0 1 0-1 1a1 1 0 0 0 1-1Z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["join_thread"] }} </span> Threads joined </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M12 19a6.995 6.995 0 0 1 10-6.32V4H2v16h10.08c-.05-.33-.08-.66-.08-1zM4 6l8 5l8-5v2l-8 5l-8-5V6zm13.34 16l-3.54-3.54l1.41-1.41l2.12 2.12l4.24-4.24L23 16.34L17.34 22z"/></svg>
        <p class="text-primary"> <span class="font-bold text-accent"> {{ data["accepted_instant_invite"] }} </span> Invites accepted </p>
      </div>

      <div class="flex flex-row gap-4 items-center"> 
        <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24"><path fill="currentColor" d="M7 5h14v2H7V5m0 8v-2h14v2H7M4 4.5A1.5 1.5 0 0 1 5.5 6A1.5 1.5 0 0 1 4 7.5A1.5 1.5 0 0 1 2.5 6A1.5 1.5 0 0 1 4 4.5m0 6A1.5 1.5 0 0 1 5.5 12A1.5 1.5 0 0 1 4 13.5A1.5 1.5 0 0 1 2.5 12A1.5 1.5 0 0 1 4 10.5M7 19v-2h14v2H7m-3-2.5A1.5 1.5 0 0 1 5.5 18A1.5 1.5 0 0 1 4 19.5A1.5 1.5 0 0 1 2.5 18A1.5 1.5 0 0 1 4 16.5Z"/></svg>
        <p class="text-primary"> Friendslist viewed <span class="font-bold text-accent"> {{ data["friends_list_viewed"] }} </span> times </p>
      </div>

    </div>
  
    <!-- <div class="bg-white"> 
      <p class="text-primary"> {{ data }}</p>
    </div> -->
  </div>
</template>

<script>
export default {
  props: {
    data: Object,
  }
}
</script>