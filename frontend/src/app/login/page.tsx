import LoginForm from "@/src/components/loginForm";

export default function LoginPage() {
  return (
    <main className="flex min-h-screen">

      <section className="hidden w-1/2 flex-col justify-center bg-slate-900 px-16 text-white md:flex">
        <h1 className="text-4xl font-bold tracking-tight">
          Your knowledge,
          <br />
          connected.
        </h1>

        <p className="mt-6 max-w-md text-lg leading-relaxed text-slate-300">
          Access organizational knowledge, discover insights, and
          find the information you need through a unified intelligent
          workspace.
        </p>
      </section>

      <section className="flex w-full items-center justify-center bg-white px-6 md:w-1/2">
        <div className="w-full max-w-md space-y-8">
          <div>
            <h2 className="text-3xl font-bold tracking-tight text-gray-900">
              Welcome back
            </h2>

            <p className="mt-2 text-sm text-gray-500">
              Sign in to your account to continue.
            </p>
          </div>

          <LoginForm />
        </div>
      </section>
    </main>
  );
}