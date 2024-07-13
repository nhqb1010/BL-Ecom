<script setup lang="ts">
const props = defineProps<{
    items?: number;
}>();
</script>

<template>
    <!-- Basket -->
    <div class="basket-icon">
        <i class="bx bx-cart"></i>

        <span v-if="props.items" class="floating-items">{{ props.items }}</span>
    </div>
</template>

<style lang="scss" scoped>
.basket-icon {
    position: relative;

    .bx {
        font-size: 30px;
        color: var(--orange-color);
    }

    .floating-items {
        position: absolute;
        top: -25%;
        right: -25%;

        display: grid;
        place-items: center;

        width: 50%;
        aspect-ratio: 1 / 1;
        border-radius: 50%;

        padding: 1px;

        font-size: 10px;
        font-weight: 600;
        font-family: var(--vn-font-family);
        color: aliceblue;
        background-color: var(--orange-color);
    }
}
</style>
