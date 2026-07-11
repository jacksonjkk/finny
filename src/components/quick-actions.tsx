export const QuickActions = () => {
  return (
    <>
      <div className="w-md p-5 border rounded-3xl space-y-3">
        <form className="flex items-center justify-between">
          <input
            placeholder="What do you need ?"
            className="border-0 outline-none focus:outiline-none focus:ring-0"
          />
          <button className="bg-primary text-white h-12 w-12 rounded-lg ml-2"></button>
        </form>

        <div className="flex items-center space-x-2 w-full">
          <button className="px-6 h-10 bg-[#BA5A31] text-white rounded-lg text-sm w-1/3">
            Get A Loan
          </button>
          <button className="px-6 h-10 bg-[#BA5A31] text-white rounded-lg text-sm w-1/3">
            Get A Loan
          </button>
          <button className="px-6 h-10 bg-[#BA5A31] text-white rounded-lg text-sm w-1/3">
            Get A Loan
          </button>
        </div>
      </div>
    </>
  );
};
