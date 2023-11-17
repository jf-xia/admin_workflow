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
import { useLocation } from "react-router-dom";

export const EntityList: React.FC<IResourceComponentsProps> = (meta) => {
  const translate = useTranslate();
  const { tableProps, tableQueryResult } = useTable({
    syncWithLocation: true,
  });

  //get current route using react-router-dom hook
  console.log(meta);

  const location = useLocation();

  const entityData = JSON.parse(localStorage.getItem("entity") || "{}").filter(
    (item: any) => "/" + item.code == location.pathname
  )[0];

  if (entityData.length === 0) {
    return (
      <List>
        <p>No data found</p>
      </List>
    );
  }

  return (
    <List>
      <Table {...tableProps} rowKey="id">
        <Table.Column dataIndex="id" title={translate("entity.fields.id")} />

        <Table.Column
          dataIndex={"payroll_date"}
          title={translate("entity.fields.payroll_date")}

          // render={(value: any) => <DateField value={value} />}
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
