<script setup lang="ts">
import { COMPANY } from "@/constants/commons";
</script>

<template>
    <section class="container introduction">
        <!-- Text -->
        <div class="introduction__text">
            <h2 class="introduction__title">
                Câu Chuyện Về
                <span>{{ COMPANY.name }}</span>
            </h2>

            <p class="introduction__description">
                Là một thương hiệu Việt Nam mang đến sứ mệnh "Nâng tầm Nông Sản
                Việt" hương vị mà Nutty Dream muốn mang đến không chỉ đơn thuần
                là một hương vị, mà còn là một tương tác tinh tế giữa đất trời
                và công lao của bà con trồng trọt. Nutty Dream mong muốn cùng
                bạn đi đến hành trình khám phá về hương vị đích thực của quê
                hương, niềm tự hào của quốc gia.
            </p>

            <p class="introduction__description">
                Or’Show trong những năm qua đã không ngừng hoàn thiện cũng như
                nâng cấp các sản phẩm để có thể đạt được những thành tựu trong
                lĩnh vực xuất khẩu các sản phẩm làm từ hạt để xuất khẩu sang các
                thị trường khó tính như Mỹ, Trung Quốc.
            </p>

            <p class="introduction__description">
                Đến năm 2024, chúng tôi chính thức thành lập Công ty TNHH Thực
                phẩm NUTTY DREAM VIETNAM với trụ sở tại TP Cần Thơ cùng mong
                muốn đem đến tay người tiêu dung Việt sản phẩm tươi ngon với hạt
                điều làm chủ đạo.
            </p>
        </div>

        <!-- Brand Image -->
        <div class="introduction__brand">
            <img
                src="../../../assets/images/intro/1.jpg"
                alt="Brand"
                class="introduction__brand-image"
            />
        </div>
    </section>
</template>

<style lang="scss" scoped>
.introduction {
    margin-top: 1.2rem;
    max-width: 1200px;
    margin-inline: auto;

    display: grid;

    &__text {
        padding: 1rem;
        margin-inline: auto;

        * {
            display: block;
            margin-inline: auto;
        }

        h2 {
            text-align: center;
            color: var(--orange-color);
            max-width: 14ch;
            margin-bottom: 2rem;
        }

        p {
            margin-top: 1.2rem;
            line-height: 1.5;
            width: 100%;
            max-width: 35ch;
            object-fit: contain;
        }
    }

    &__brand {
        display: grid;
        place-items: center;

        img {
            width: 85%;
            max-width: 28em;
            // padding: 0.5rem;
            aspect-ratio: 1 / 1;
            border-radius: 20px;
            object-fit: cover;
            box-shadow: rgba(255, 255, 255, 0.1) 0px 1px 1px 0px inset,
                rgba(50, 50, 93, 0.25) 0px 50px 100px -20px,
                rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
        }
    }
}

@media (min-width: 768px) {
    .introduction {
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));

        &__text {
            margin-left: auto;
            margin-right: initial;

            p {
                max-width: 50ch;
                font-size: 1.1rem;
            }
        }
    }
}
</style>
