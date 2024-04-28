<script setup lang="ts">
import { useCounterStore } from "../stores/counter";
import { storeToRefs } from "pinia";

const counterStore = useCounterStore();
const { count, doubleCount } = storeToRefs(counterStore);
</script>

<template>
    <div class="counter__container">
        <h2>Counter</h2>
        <p>Count: {{ count }}</p>
        <p>Double Count: {{ doubleCount }}</p>
        <button @click="counterStore.increment()">Increment</button>
    </div>
</template>

<style scoped></style>
