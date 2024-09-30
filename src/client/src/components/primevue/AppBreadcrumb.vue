<script setup lang="ts">
import { defineProps } from "vue";

import Breadcrumb from "primevue/breadcrumb";

// Define the types for props
interface Home {
    icon: string;
    routeName: string;
}

interface Item {
    label: string;
    routeName?: string;
    icon?: string;
    url?: string;
    target?: string;
}

// Define the props
const props = defineProps<{
    home: Home;
    items: Item[];
}>();
</script>

<template>
    <Breadcrumb :home="props.home" :model="props.items" class="app-breadcrumb">
        <template #item="{ item, props }">
            <!-- Vue router internal links -->
            <router-link
                v-if="item.routeName"
                :to="{ name: item.routeName }"
                class="href-link breadcrumb-link breadcrumb-label"
            >
                <i v-if="item.icon" :class="[item.icon, 'breadcrumb-icon']" />
                {{ item.label }}
            </router-link>

            <!-- external links -->
            <a
                v-else-if="item.url"
                :href="item.url"
                :target="item.target"
                v-bind="props.action"
                class="href-link breadcrumb-link breadcrumb-label"
            >
                {{ item.label }}
            </a>

            <!-- Normal Label -->
            <p class="breadcrumb-normal breadcrumb-label" v-else>
                {{ item.label }}
            </p>
        </template>
    </Breadcrumb>
</template>

<style lang="scss" scoped>
.app-breadcrumb {
    --p-breadcrumb-background: transparent;
    --p-breadcrumb-gap: 0.25rem;
    --p-icon-size: 0.6rem;

    .breadcrumb-label {
        max-width: 22ch;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .breadcrumb-icon {
        font-size: 1.2rem;
        color: var(--orange-color);
    }

    .breadcrumb-link {
        font-size: 0.95rem;
        color: var(--light-orange-color);

        &:hover {
            color: var(--orange-color);
        }
    }

    .breadcrumb-normal {
        font-size: 1rem;
        font-weight: 600;
        color: var(--orange-color);
    }

    @media (min-width: 820px) {
        .breadcrumb-label {
            max-width: auto;
            font-size: 1.3rem;
        }

        .breadcrumb-icon {
            font-size: 1.6rem;
        }
    }
}
</style>
