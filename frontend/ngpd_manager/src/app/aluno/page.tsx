"use client";

import { useState } from "react";
import { useForm, ValidateResult } from "react-hook-form";
import type { Aluno } from "./interfaces";

export default function Aluno() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const [name, setName] = useState("");
  const pessoa: Partial<Aluno> = {};


  const validateUsername = (value: string): ValidateResult => {
    return value ? true : "Nome de usuário é obrigatório";
  };

  const validatePassword = (value: string): ValidateResult => {
    return value ? true : "Senha é obrigatória";
  };

  const validatePasswordComplexity = (value: string): ValidateResult => {
    return value.length > 10 ? true : "Essa senha não atende aos critérios";
  };

  const onSubmit = (data: any) => {

  };

  return (
    <>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input
          {...register("username", { validate: validateUsername })}
        />
        {errors.username && <span>{String(errors.username.message)}</span>}
        <input
          type="password"
          {...register("password", {
            validate: {
              validatePassword,
              validatePasswordComplexity
            }
          })}
          placeholder="Senha"
        />
        {errors.password && <span>{String(errors.password.message)}</span>}
        <button type="submit">Exibir Valor</button>
      </form>
      <span>{name}</span>
    </>
  );
}