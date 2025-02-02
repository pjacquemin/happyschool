// This file is part of Happyschool.
//
// Happyschool is the legal property of its developers, whose names
// can be found in the AUTHORS file distributed with this source
// distribution.
//
// Happyschool is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Happyschool is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with Happyschool.  If not, see <http://www.gnu.org/licenses/>.

import Vue from "vue";

import store from "../schedule_change/store.js";
import router from "../schedule_change/router.js";

import AppMenu from "../common/menu_bar.vue";


new Vue({
    el: "#vue-app",
    data: {
        fullscreen: false,
        menuInfo: {},
        transitionName: "slide-left",
    },
    store,
    router,
    template: `
    <div>
        <app-menu v-if="!fullscreen" :menu-info="menuInfo" />
        <transition :name="transitionName" mode="out-in">
            <router-view></router-view>
        </transition>
    </div>`,
    components: { AppMenu },
    mounted: function () {
        // eslint-disable-next-line no-undef
        this.menuInfo = menu;

        this.$store.dispatch("getChangeType");
        this.$store.dispatch("getChangeCategory");

        this.fullscreen = window.location.href.includes("fullscreen");
    },
    watch: {
        "$route" (to, from) {
            const toDepth = to.path.split("/").length;
            const fromDepth = from.path.split("/").length;
            this.transitionName = toDepth < fromDepth ? "slide-right" : "slide-left";
        }
    }
});
