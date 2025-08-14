import Link from 'next/link';
import Image from 'next/image';

// You can create a separate component for icons if you use them frequently
const CheckIcon = () => (
  <svg className="w-6 h-6 text-green-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7"></path></svg>
);

export default function Home() {
  return (
    <>
      {/* Hero Section */}
      <section className="bg-blue-700 text-white text-center py-20">
        <h1 className="text-4xl md:text-5xl font-bold">الحماية الرقمية التي تستحقها</h1>
        <p className="mt-4 text-lg md:text-xl max-w-2xl mx-auto">
          نوفر حلول أمن سيبراني متكاملة لحماية أعمالك من التهديدات الرقمية المتطورة.
        </p>
        <Link href="/contact" className="mt-8 inline-block bg-white text-blue-700 font-bold py-3 px-8 rounded-full hover:bg-gray-200 transition-colors">
          احصل على استشارة مجانية
        </Link>
      </section>

      {/* Featured Services Section */}
      <section className="py-16 bg-white">
        <div className="text-center">
          <h2 className="text-3xl font-bold text-gray-800">خدماتنا وحلولنا</h2>
          <p className="text-gray-600 mt-2">نقدم مجموعة شاملة من الخدمات لتلبية احتياجاتك الأمنية والشبكية.</p>
        </div>
        <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Service Card 1 */}
          <div className="p-8 border rounded-lg shadow-md hover:shadow-xl transition-shadow">
            <h3 className="text-xl font-bold">استشارات الأمن السيبراني</h3>
            <p className="mt-2 text-gray-600">تقييم شامل للبنية التحتية الخاصة بك وتقديم توصيات مخصصة.</p>
          </div>
          {/* Service Card 2 */}
          <div className="p-8 border rounded-lg shadow-md hover:shadow-xl transition-shadow">
            <h3 className="text-xl font-bold">تصميم وتركيب الشبكات</h3>
            <p className="mt-2 text-gray-600">حلول شبكية موثوقة وعالية الأداء من أفضل العلامات التجارية.</p>
          </div>
          {/* Service Card 3 */}
          <div className="p-8 border rounded-lg shadow-md hover:shadow-xl transition-shadow">
            <h3 className="text-xl font-bold">الدعم الفني والصيانة</h3>
            <p className="mt-2 text-gray-600">عقود صيانة ودعم فني لضمان استمرارية أعمالك دون انقطاع.</p>
          </div>
        </div>
      </section>

      {/* Our Brands Section */}
      <section className="py-12 bg-gray-100">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-700">شركاؤنا من العلامات التجارية العالمية</h2>
        </div>
        <div className="mt-8 flex justify-center items-center space-x-8 md:space-x-16">
          <p className="text-2xl font-bold text-gray-500">Fortinet</p>
          <p className="text-2xl font-bold text-gray-500">Ruijie</p>
          <p className="text-2xl font-bold text-gray-500">Grandstream</p>
        </div>
      </section>

      {/* Why Choose Us Section */}
      <section className="py-16 bg-white">
        <div className="text-center">
          <h2 className="text-3xl font-bold text-gray-800">لماذا تختار SafeDeny؟</h2>
        </div>
        <div className="mt-12 grid md:grid-cols-2 gap-8 items-center">
          <div>
            {/* Placeholder for an image */}
            <div className="bg-gray-300 w-full h-64 rounded-lg"></div>
          </div>
          <ul className="space-y-4">
            <li className="flex items-start"><CheckIcon /> <span><b>خبرة متخصصة:</b> فريق من الخبراء المعتمدين في الأمن السيبراني والشبكات.</span></li>
            <li className="flex items-start"><CheckIcon /> <span><b>حلول متكاملة:</b> نقدم كل ما تحتاجه من الأجهزة والبرامج والخدمات في مكان واحد.</span></li>
            <li className="flex items-start"><CheckIcon /> <span><b>دعم استثنائي:</b> نلتزم بتقديم دعم فني سريع وفعال لضمان رضا عملائنا.</span></li>
            <li className="flex items-start"><CheckIcon /> <span><b>شراكات موثوقة:</b> وكلاء معتمدون لأفضل العلامات التجارية في العالم.</span></li>
          </ul>
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="py-16 bg-gray-100">
        <div className="text-center">
          <h2 className="text-3xl font-bold text-gray-800">ماذا يقول عملاؤنا</h2>
        </div>
        <div className="mt-12 grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Testimonial 1 */}
          <div className="p-6 bg-white rounded-lg shadow-md">
            <p className="text-gray-600">"كانت خدمة SafeDeny ممتازة. ساعدونا في تأمين شبكتنا بالكامل بكفاءة عالية واحترافية. نوصي بهم بشدة."</p>
            <p className="mt-4 font-bold text-right">- شركة تكنولوجيا المستقبل</p>
          </div>
          {/* Testimonial 2 */}
          <div className="p-6 bg-white rounded-lg shadow-md">
            <p className="text-gray-600">"فريق الدعم الفني لديهم هو الأفضل. استجابتهم سريعة وحلولهم فعالة. نحن نشعر بأمان أكبر الآن."</p>
            <p className="mt-4 font-bold text-right">- المجموعة المالية المتحدة</p>
          </div>
        </div>
      </section>
    </>
  );
}
