<script setup lang="ts"></script>

<template>
    <header>
        <!-- Basket Icon -->
        <a href="#" class="nav__logo"><i class="bx bx-basket"></i>Delicacy</a>

        <!-- Menu Icon -->
        <div class="bx bx-menu" id="menu-icon"></div>

        <!-- Navbar Links -->
        <ul class="nav__links">
            <li class="nav__link"><a class="active" href="#home">Home</a></li>
            <li class="nav__link"><a href="#categories">Categories</a></li>
            <li class="nav__link"><a href="#products">Products</a></li>
            <li class="nav__link"><a href="#about">About</a></li>
            <li class="nav__link"><a href="#customers">Customers</a></li>
        </ul>

        <!-- Profile -->
        <div class="nav__profile">
            <img src="../assets/images/profile.jpg" alt="profile-avatar" />
            <span>John Doe</span>
            <i class="bx bx-caret-down"></i>
        </div>
    </header>
</template>

<style lang="scss" scoped>
header {
    position: fixed;
    width: 100%;
    top: 0;
    right: 0;
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 20px 100px;
    background: var(--bg-color);
    box-shadow: rgba(0, 0, 0, 0.02) 0px 1px 3px 0px,
        rgba(27, 31, 35, 0.15) 0px 0px 0px 1px;
    transition: 0.5s;

    .nav__logo {
        display: flex;
        align-items: center;
        font-size: 1.1rem;
        font-weight: 600;
        color: var(--text-color);
        gap: 0.5rem;

        .bx {
            font-size: 24px;
            color: var(--orange-color);
        }
    }

    .nav__links {
        display: flex;
        gap: 0.5rem;

        .nav__link {
            a {
                font-size: 1rem;
                font-weight: 500;
                color: var(--text-color);
                padding: 0.5rem 1rem;

                &:hover,
                &.active {
                    background-color: var(--green-color);
                    color: var(--bg-color);
                    border-radius: 5rem;
                    transition: background 0.5s ease-in;
                }
            }
        }
    }

    .nav__profile {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        cursor: pointer;

        img {
            width: 40px;
            aspect-ratio: 1/1;
            object-fit: cover;
            object-position: center;
            border-radius: 50%;
        }

        span {
            font-size: 13px;
            font-weight: 500;
        }
    }

    #menu-icon {
        display: none;
        font-size: 24px;
        color: var(--text-color);
        cursor: pointer;
        z-index: 1001;
    }
}
</style>
