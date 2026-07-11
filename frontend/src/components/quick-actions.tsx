export const QuickActions = () => {
  return (
    <section className="flex items-center space-y-10 flex-col">
      <div className="w-sm text-center">
        <h1 className="text-3xl">Welcome Back, Jerome !</h1>
      </div>
      <div className="w-xl p-5 border rounded-3xl space-y-3">
        <form className="flex items-center justify-between">
          <input
            placeholder="What do you need ?"
            className="border-0 outline-none focus:outiline-none focus:ring-0"
          />
          <button className="bg-primary/70 text-white h-12 w-12 rounded-lg ml-2"></button>
        </form>

        <div className="flex items-center space-x-2 w-full">
          <button className="px-6 h-10 bg-teal-800/60 text-white rounded-lg text-sm w-1/3">
            Get A Loan
          </button>
          <button className="px-6 h-10 bg-yellow-800/60 text-white rounded-lg text-sm w-1/3">
            History
          </button>
          <button className="px-6 h-10 bg-[#BA5A31]/60 text-white rounded-lg text-sm w-1/3">
            Providers
          </button>
        </div>
      </div>
      <p className="text-xs w-md text-center text-black/60">
        Finny is an AI. It can make mistakes, please review the output
      </p>
    </section>
  );
};
