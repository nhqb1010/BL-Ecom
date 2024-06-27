<script setup lang="ts">
import { ref } from "vue";

import PVButton from "primevue/button";
import InputText from "primevue/inputtext";

const email = ref<string>("");
</script>

<template>
    <div class="home-join-us home-join-us__container">
        <div class="home-join-us__content">
            <h2 class="home-join-us__content-title">
                Hãy trở thành một phần của chúng tôi
            </h2>
            <p class="home-join-us__content-description">
                Đăng ký để nhận thông tin mới nhất từ chúng tôi
            </p>

            <div class="home-join-us__input">
                <InputText
                    type="email"
                    placeholder="quocbao.ngoh@gmail.com"
                    v-model="email"
                />
                <PVButton>
                    <i class="bx bxs-envelope"></i>
                </PVButton>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.home-join-us {
    max-width: 1200px;
    width: 90%;
    border-radius: 2rem;
    background: linear-gradient(
        to right,
        var(--green-color),
        var(--light-green-color)
    );
    margin-inline: auto;
    padding: 3rem;
    text-align: center;

    h2 {
        width: 100%;
        margin-inline: auto;
        margin-bottom: 2rem;
        line-height: 1.7;
    }

    p {
        min-width: 20ch;
        line-height: 1.5;
        margin-inline: auto;
        text-align: center;
    }

    &__input {
        margin-top: 1rem;
        margin-inline: auto;
        width: min(90%, 550px);

        display: flex;

        input {
            flex-grow: 1;
            line-height: 2;
            border-radius: 0;
            border-bottom-left-radius: 5px;
            border-top-left-radius: 5px;
        }

        button {
            background-color: var(--light-orange-color);
            border: none;
            border-radius: 0;
            border-bottom-right-radius: 5px;
            border-top-right-radius: 5px;

            i {
                font-size: 1.5rem;

                transition: all 0.2s ease;
            }

            &:hover {
                background-color: var(--orange-color);
                border: none;
            }
        }
    }

    @media (min-width: 584px) {
        padding-inline: 4rem;

        .home-join-us__input {
            margin-top: 2rem;
        }
    }

    @media (min-width: 768px) {
        padding: 5rem 10rem;
    }
}
</style>
