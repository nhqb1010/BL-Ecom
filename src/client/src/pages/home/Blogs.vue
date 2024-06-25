<script setup lang="ts">
import BlogCard from "@/components/BlogCard.vue";
import type { IBlogCardProps } from "@/types/blogs";

const blogs: IBlogCardProps[] = [
    {
        imageUrl: "https://picsum.photos/300/300",
        title: "Chiều cùng ngày, Thủ tướng Phạm Minh Chính tiếp lãnh đạo một số doanh nghiệp Trung Quốc",
        description:
            "Chiều cùng ngày, Thủ tướng Phạm Minh Chính tiếp lãnh đạo một số doanh nghiệp Trung Quốc: Ông Tôn Vinh Khôn, Chủ tịch Công ty Đầu máy toa xe Đại Liên; ông Vương Tiểu Quân, Phó Chủ tịch Tập đoàn xây dựng Điện lực Trung Quốc",
    },
    {
        imageUrl: "https://picsum.photos/301/300",
        title: "Bài viết 2",
        description:
            "Chiều cùng ngày, Thủ tướng Phạm Minh Chính tiếp lãnh đạo một số doanh nghiệp Trung Quốc: Ông Tôn Vinh Khôn, Chủ tịch Công ty Đầu máy toa xe Đại Liên; ông Vương Tiểu Quân, Phó Chủ tịch Tập đoàn xây dựng Điện lực Trung Quốc",
    },
    {
        imageUrl: "https://picsum.photos/302/300",
        title: "Bài viết 3",
        description:
            "Chiều cùng ngày, Thủ tướng Phạm Minh Chính tiếp lãnh đạo một số doanh nghiệp Trung Quốc ...",
    },
];
</script>

<template>
    <div class="container home-blogs">
        <h2 class="home-blogs__title">Bài Viết</h2>

        <div class="home-blogs__content">
            <div class="blogs-list">
                <BlogCard
                    v-for="(blog, index) of blogs"
                    :key="index"
                    v-bind="blog"
                />
            </div>
            <div class="blogs-more">
                <a href="#" class="btn-link">
                    Xem thêm <i class="bx bx-right-arrow-alt"></i>
                </a>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.home-blogs {
    margin-block: 2.2rem;
    max-width: 1200px;
    width: 90%;
    margin-inline: auto;

    &__title {
        text-align: center;
        color: var(--orange-color);
        margin-inline: auto;
        margin-bottom: 2rem;
    }

    &__content {
        .blogs-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2.5rem;
        }

        .blogs-more {
            margin-block: 1.5rem;
            width: 100%;
            display: grid;
            place-items: center;
        }
    }
}
</style>
