<script setup lang="ts">
import { COMPANY } from "@/constants/commons";
</script>

<template>
    <div class="about about__container">
        <div class="about__header">
            <h1 class="title">
                <span class="highlight">Nutty Dream Vietnam</span> và
                <span class="highlight">{{ COMPANY.name }}</span>
            </h1>
        </div>

        <div class="about__info">
            <p>
                Nutty Dream Vietnam với giấc mơ mang đến hương vị đặc trưng của
                hạt điều Việt Nam đến với mọi người trên khắp thế giới. Từ những
                vùng đất xinh đẹp mang vẻ đẹp đặc trưng của đất nước hình chữ S
                - nông sản chính là cái tâm, cái tầm của đất nước, sản phẩm hạt
                điều của chúng tôi cam kết đầy đủ các giấy tờ chứng nhận liên
                quan đến Quản lý ATTP, ISO 22000:2018, HACCP.
            </p>

            <p>
                Nutty Dream đặt mục tiêu trở thành nhà sản và phân phối các sản
                phẩm làm từ hạt đứng đầu Việt Nam. Đem đến những sản phẩm với
                giá trị dinh dưỡng tốt cho người tiêu dùng, đồng thời thực hiện
                các hoạt động trách nhiệm xã hội
            </p>

            <div class="image-container">
                <img src="../assets/images/about/5.jpg" alt="about_1" />
            </div>

            <p>
                Or’Show trong những năm qua đã không ngừng hoàn thiện cũng như
                nâng cấp các sản phẩm để có thể đạt được những thành tựu trong
                lĩnh vực xuất khẩu các sản phẩm làm từ hạt để xuất khẩu sang các
                thị trường khó tính như Mỹ, Trung Quốc.
            </p>

            <p>
                Đến năm 2024, chúng tôi chính thức thành lập Công ty TNHH Thực
                phẩm NUTTY DREAM VIETNAM với trụ sở tại TP Cần Thơ cùng mong
                muốn đem đến tay người tiêu dung Việt sản phẩm tươi ngon với hạt
                điều làm chủ đạo.
            </p>

            <div class="image-container">
                <img src="../assets/images/about/16.jpg" alt="about_1" />
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.about {
    margin-inline: auto;
    max-width: 1000px;

    margin-top: var(--nav-height);
    padding: 1rem;

    &__header {
        .title {
            font-size: 1.5rem;
            font-weight: 500;
            line-height: 1.5;

            width: 100%;
            text-align: center;

            span.highlight {
                color: var(--orange-color);
                font-weight: 700;
                white-space: nowrap;
            }
        }
    }

    &__info {
        p {
            margin-top: 1rem;
            margin-bottom: 0 !important;

            font-size: 1rem;
            line-height: 1.7;
        }

        .image-container {
            margin-block: 2rem;
            margin-inline: auto;
            width: 85%;
            max-width: 32em;

            img {
                width: 100%;
                border-radius: 0.5rem;
                box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
                    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
            }
        }
    }

    @media screen and (min-width: 868px) {
        &__header {
            .title {
                font-size: 2rem;
                font-weight: 700;
            }
        }

        &__info {
            p {
                font-size: 1.1rem;
            }
        }
    }
}
</style>
