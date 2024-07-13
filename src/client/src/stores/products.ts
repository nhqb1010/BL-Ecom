import { defineStore } from "pinia";
import { computed, ref } from "vue";

import type { IProductDetailType } from "@/types/products";

import { getProducts } from "@/api/products";

export const useProductsStore = defineStore("products", () => {
    const products = ref<IProductDetailType[]>([]);
    const loading = ref(false);

    const fetchProducts = async () => {
        loading.value = true;
        products.value = await getProducts();
        loading.value = false;
    };

    const featuredProducts = computed(() => products.value.slice(0, 2) ?? []);

    return { products, featuredProducts, loading, fetchProducts };
});
