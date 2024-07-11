/** @odoo-module **/

import { registry } from '@web/core/registry';

const {  useState, Component } = owl;

export class OwlTodoList extends Component {
    setup() {
        this.state = useState({
            taskList: [1, 2, 3],
        });
    }
}

OwlTodoList.template = 'owl_custom.TodoList';

registry.category('actions').add('owl_custom.TodoList', OwlTodoList);
