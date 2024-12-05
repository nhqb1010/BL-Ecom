<template>
    <div class="container">
        <h3>
            <i class="bx bxs-ghost"></i>
            Trang Không Tồn Tại
            <i class="bx bxs-ghost"></i>
        </h3>

        <RouterLink :to="{ name: 'Home' }" class="href-link">
            <i class="bx bxs-hand-right"></i>
            Trang Chủ
            <i class="bx bxs-hand-right" style="transform: scale(-1, 1)"></i>
        </RouterLink>
    </div>
</template>

<style lang="scss" scoped>
.container {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    i {
        color: var(--orange-color);
    }

    a {
        margin-top: 3rem;
        font-size: 1.3rem;
        color: var(--green-color);

        &:hover {
            text-decoration: underline;
        }
    }
}
</style>
