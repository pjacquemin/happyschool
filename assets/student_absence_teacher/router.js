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

import StudentAbsenceTeacher from "./student_absence_teacher.vue";
import AddAbsence from "./add_absence.vue";
import ListAbsence from "./list_absence.vue";
import Overview from "./overview.vue";

export default new VueRouter({
    routes: [
        {
            path: "",
            component: StudentAbsenceTeacher,
            children: [
                {
                    path: "",
                    component: AddAbsence,
                },
                {
                    path: "add_absence",
                    component: AddAbsence,
                },
                {
                    path: "list",
                    component: ListAbsence,
                },
                {
                    path: "overview",
                    component: Overview,
                },
            ],
        }
    ]
});
