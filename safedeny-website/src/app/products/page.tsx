import Link from 'next/link';
import { Product } from '@/types';

// This function will run on the server
async function getProducts(): Promise<Product[]> {
  // We need to use an absolute URL for fetch on the server.
  const baseUrl = process.env.VERCEL_URL ? `https://${process.env.VERCEL_URL}` : 'http://localhost:3000';
  const res = await fetch(`${baseUrl}/api/products`, { cache: 'no-store' }); // Disable cache for development

  if (!res.ok) {
    throw new Error('Failed to fetch products');
  }
  return res.json();
}

export default async function ProductsPage() {
  const products = await getProducts();

  // Get unique categories
  const categories = [...new Set(products.map(p => p.category))];

  return (
    <div className="py-12">
      <div className="text-center">
        <h1 className="text-4xl font-bold text-gray-800">كتالوج المنتجات</h1>
        <p className="mt-2 text-lg text-gray-600">تصفح منتجاتنا حسب الفئة</p>
      </div>

      <div className="mt-12 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
        {categories.map(category => (
          <Link
            key={category}
            href={`/products/category/${encodeURIComponent(category)}`}
            className="block p-8 bg-white rounded-lg shadow-md hover:shadow-xl hover:bg-blue-50 transition-all duration-300"
          >
            <h2 className="text-2xl font-bold text-center text-gray-800">{category}</h2>
          </Link>
        ))}
      </div>
    </div>
  );
}
