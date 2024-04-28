<script setup lang="ts">
import Counter from "../components/Counter.vue";
</script>

<template>
    <main>
        <h1>This is from the home page</h1>

        <!-- Counter Section -->
        <Counter />
    </main>
</template>

<style scoped>
main {
    width: 100%;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
</style>
