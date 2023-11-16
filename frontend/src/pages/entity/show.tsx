import React from "react";
import {
  IResourceComponentsProps,
  useShow,
  useTranslate,
} from "@refinedev/core";
import {
  Show,
  NumberField,
  TagField,
  TextField,
  DateField,
} from "@refinedev/antd";
import { Typography } from "antd";

const { Title } = Typography;

export const EntityShow: React.FC<IResourceComponentsProps> = () => {
  const translate = useTranslate();
  const { queryResult } = useShow();
  const { data, isLoading } = queryResult;

  const record = data?.data;

  return (
    <Show isLoading={isLoading}>
      <Title level={5}>{translate("entity.fields.id")}</Title>
      <NumberField value={record?.id ?? ""} />
      <Title level={5}>{translate("entity.fields.employee_code")}</Title>
      <TextField value={record?.employee_code} />
      <Title level={5}>{translate("entity.fields.employee_category")}</Title>
      <TextField value={record?.employee_category} />
      <Title level={5}>{translate("entity.fields.employee_mode")}</Title>
      <TextField value={record?.employee_mode} />
      <Title level={5}>{translate("entity.fields.payroll_date")}</Title>
      <DateField value={record?.payroll_date} />
      <Title level={5}>{translate("entity.fields.charging_department")}</Title>
      <TextField value={record?.charging_department} />
      <Title level={5}>{translate("entity.fields.charging_cost_centre")}</Title>
      <NumberField value={record?.charging_cost_centre ?? ""} />
      <Title level={5}>{translate("entity.fields.project_code")}</Title>
      <NumberField value={record?.project_code ?? ""} />
      <Title level={5}>{translate("entity.fields.submitted_by")}</Title>
      <NumberField value={record?.submitted_by ?? ""} />
      <Title level={5}>{translate("entity.fields.submitted_at")}</Title>
      <DateField value={record?.submitted_at} />
      <Title level={5}>{translate("entity.fields.submitted_contact")}</Title>
      <NumberField value={record?.submitted_contact ?? ""} />
    </Show>
  );
};
