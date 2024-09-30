<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { useRouter } from "vue-router";

import { useWindowScroll } from "@vueuse/core";
import PVButton from "primevue/button";
import PVInputNumber from "primevue/inputnumber";

import type { IProductDetailType } from "@/types/products";

import { getProductById } from "@/api/products";
import AppBreadcrumb from "@/components/primevue/AppBreadcrumb.vue";
import { getValue, transformToVNDFormat } from "@/utils";
import { PRODUCT_PROPS_LABELS } from "../constant";

const breadcrumbContents: any = ref({
    home: {
        icon: "bx bxs-home-alt-2",
        routeName: "Home",
    },
    items: [{ label: "Sản Phẩm", routeName: "Products" }],
});

const router = useRouter();
const { x, y } = useWindowScroll({ behavior: "smooth" });
const productId = computed(() => router.currentRoute.value.params?.id);
const product = ref<IProductDetailType | null>(null);

const quantity = ref(1);
const productProps = {
    weight: "30 gram",
    basketWeight: "30 gram",
    expTime: "12 tháng",
};

onMounted(async () => {
    product.value = await getProductById(productId.value);

    if (!product.value) {
        router.replace({ name: "404" });
    }

    breadcrumbContents.value.items.push({ label: product.value?.name! });
    x.value = 0;
    y.value = 0;
});
</script>

<template>
    <section class="container product-detail">
        <!-- Breadcrumbs -->
        <AppBreadcrumb
            :home="breadcrumbContents.home"
            :items="breadcrumbContents.items"
        />

        <!-- Product Detail -->
        <div v-if="product" class="product-detail__info product-detail">
            <div class="product-detail__image">
                <img :src="product?.imageUrl" alt="Product Image" />
            </div>

            <div class="product-detail__price-info">
                <h3>{{ product?.name }}</h3>

                <p class="description">{{ product.description }}</p>

                <p class="product-prop" v-for="(value, key) in productProps">
                    <span>
                        {{ getValue(key, PRODUCT_PROPS_LABELS, "--") }}:
                    </span>
                    {{ value }}
                </p>

                <p class="pricing-text">
                    {{ transformToVNDFormat(product?.price!) }}
                </p>

                <!-- Buy Buttons -->
                <div class="button-groups">
                    <!-- Quantity -->
                    <PVInputNumber
                        v-model="quantity"
                        inputId="quantity"
                        showButtons
                        buttonLayout="horizontal"
                        :step="1"
                        :min="1"
                        :max="10"
                        fluid
                        inputClass="small-text-input"
                    >
                        <template #incrementbuttonicon>
                            <i class="inc-icon bx bx-plus"></i>
                        </template>
                        <template #decrementbuttonicon>
                            <i class="inc-icon bx bx-minus"></i>
                        </template>
                    </PVInputNumber>

                    <!-- Add to Basket -->
                    <PVButton label="Thêm vào giỏ hàng" icon="bx bx-basket" />
                </div>
            </div>
        </div>
    </section>
</template>

<style lang="scss" scoped>
.container {
    margin-block: 5rem;
    margin-inline: auto;
    width: 95%;

    .product-detail {
        &__image {
            img {
                width: 100%;
                aspect-ratio: 1 / 1;
                object-fit: fit;
                border-radius: 2rem;
            }
        }

        &__price-info {
            padding-inline: 0.5rem;

            h3 {
                font-size: 1.5rem;
                font-weight: 700;
                margin-block: 1rem;
                line-height: 1.2;
            }

            .description {
                font-weight: 400;
                line-height: 1.4;
                text-align: justify;
                margin-block: 1rem;
            }

            .product-prop {
                line-height: 1.4;
                margin-bottom: 1rem;

                span {
                    font-weight: 600;
                }
            }

            .pricing-text {
                font-size: 1.3rem;
                font-weight: 600;
                margin-block: 2rem;
            }

            .button-groups {
                display: flex;
                gap: 1rem;
                align-items: center;
                margin-block: 1.2rem;

                .inc-icon {
                    font-size: 1.2rem;
                    font-weight: 1000;
                    color: var(--orange-color);
                }
            }
        }
    }

    @media (min-width: 584px) {
        max-width: 584px;
    }

    @media (min-width: 820px) {
        max-width: 1200px;

        .product-detail {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;

            &__image {
                img {
                    aspect-ratio: 1 / 1.2;
                    object-fit: cover;
                }
            }
        }
    }

    @media (min-width: 920px) {
        .product-detail {
            max-width: 950px;
            margin-inline: auto;
            &__image {
                img {
                    aspect-ratio: 1 / 1;
                    object-fit: fit;
                }
            }
        }
    }
}
</style>
