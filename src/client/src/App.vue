<script setup lang="ts">
import { ref, watch } from "vue";
import { useRouter } from "vue-router";

import AppFooter from "./components/AppFooter.vue";
import AppNav from "./components/NavBar/AppNav.vue";

const router = useRouter();
const noAuthLayout = ref<boolean>(false);

watch(
    () => router.currentRoute.value,
    (to, from) => {
        noAuthLayout.value = !!to.meta.noAuth;
    }
);
</script>

<template>
    <!-- Nav bar -->
    <AppNav v-if="!noAuthLayout" />

    <!-- Page View -->
    <RouterView />

    <!-- Footer -->
    <AppFooter v-if="!noAuthLayout" />
</template>
