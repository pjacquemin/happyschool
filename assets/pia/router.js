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
import VueRouter from "vue-router";

Vue.use(VueRouter);

import PiaPage from "../pia/pia_page.vue";
import PiaRecord from "../pia/pia_record.vue";

export default new VueRouter({
    routes: [
        {
            path: "/",
            component: PiaPage,
        },
        {
            path: "/page/:currentPage/",
            component: PiaPage,
            props: true,
        },
        {
            path: "/edit/:id/:advanced/",
            component: PiaRecord,
            props: (route) => {
                const props = { ...route.params };
                props.advanced = props.advanced === "true";
                return props;
            }
        },
        {
            path: "/new/:advanced/",
            component: PiaRecord,
            props: (route) => {
                const props = { ...route.params };
                props.advanced = props.advanced === "true";
                return props;
            }
        },
    ]
});
