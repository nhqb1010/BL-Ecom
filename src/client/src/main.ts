import "./assets/css/main.scss";

import Aura from "@primevue/themes/aura";
import PrimeVue from "primevue/config";

import { createPinia } from "pinia";
import { createApp } from "vue";

import App from "./App.vue";
import router from "./router";

const app = createApp(App);
app.use(PrimeVue, {
    theme: {
        preset: Aura,
        options: {
            prefix: "p",
            darkModeSelector: "",
            cssLayer: false,
        },
    },
});

app.use(createPinia());
app.use(router);

app.mount("#app");
