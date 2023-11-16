import React from "react";
import {
  IResourceComponentsProps,
  BaseRecord,
  useTranslate,
} from "@refinedev/core";
import {
  useTable,
  List,
  EditButton,
  ShowButton,
  DeleteButton,
  DateField,
} from "@refinedev/antd";
import { Table, Space } from "antd";

export const EntityList: React.FC<IResourceComponentsProps> = () => {
  const translate = useTranslate();
  const { tableProps } = useTable({
    syncWithLocation: true,
  });

  return (
    <List>
      <Table {...tableProps} rowKey="id">
        <Table.Column dataIndex="id" title={translate("entity.fields.id")} />
        <Table.Column
          dataIndex="employee_code"
          title={translate("entity.fields.employee_code")}
        />
        <Table.Column
          dataIndex="employee_category"
          title={translate("entity.fields.employee_category")}
        />
        <Table.Column
          dataIndex="employee_mode"
          title={translate("entity.fields.employee_mode")}
        />
        <Table.Column
          dataIndex={["payroll_date"]}
          title={translate("entity.fields.payroll_date")}
          render={(value: any) => <DateField value={value} />}
        />
        <Table.Column
          dataIndex="charging_department"
          title={translate("entity.fields.charging_department")}
        />
        <Table.Column
          dataIndex="charging_cost_centre"
          title={translate("entity.fields.charging_cost_centre")}
        />
        <Table.Column
          dataIndex="project_code"
          title={translate("entity.fields.project_code")}
        />
        <Table.Column
          dataIndex="submitted_by"
          title={translate("entity.fields.submitted_by")}
        />
        <Table.Column
          dataIndex={["submitted_at"]}
          title={translate("entity.fields.submitted_at")}
          render={(value: any) => <DateField value={value} />}
        />
        <Table.Column
          dataIndex="submitted_contact"
          title={translate("entity.fields.submitted_contact")}
        />
        <Table.Column
          title={translate("table.actions")}
          dataIndex="actions"
          render={(_, record: BaseRecord) => (
            <Space>
              <EditButton hideText size="small" recordItemId={record.id} />
              <ShowButton hideText size="small" recordItemId={record.id} />
              <DeleteButton hideText size="small" recordItemId={record.id} />
            </Space>
          )}
        />
      </Table>
    </List>
  );
};
