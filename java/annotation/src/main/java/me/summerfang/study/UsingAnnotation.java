package me.summerfang.study;

import java.lang.annotation.Annotation;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class UsingAnnotation {
    public static void main(String[] args) throws NoSuchMethodException, SecurityException, NoSuchFieldException {
        Class aClass = TheClass.class;

        Annotation[] annotations = aClass.getAnnotations();

        for(Annotation annotation: annotations) {
            if (annotation instanceof MyAnnotation) {
                MyAnnotation myAnnotation = (MyAnnotation) annotation;
                System.out.println(myAnnotation.name());
                System.out.println(myAnnotation.value());
            }
        }


        Annotation anno = aClass.getAnnotation(MyAnnotation.class);
        if (anno instanceof MyAnnotation) {
            MyAnnotation myAnno = (MyAnnotation) anno;
            System.out.println(myAnno.name());
            System.out.println(myAnno.value());
        }

        // Method method = aClass.getMethod("doSomething", null);
        // annotations = method.getDeclaredAnnotations();

        // for (Annotation annotation: annotations) {
        //     if (annotation instanceof MyAnnotation) {
        //         MyAnnotation myAnnotation = (MyAnnotation) annotation;
        //         System.out.println(myAnnotation.name());
        //         System.out.println(myAnnotation.value());
        //     }
        // }

        // Annotation annotation = method.getAnnotation(MyAnnotation.class);
        // if (annotation instanceof MyAnnotation) {
        //     MyAnnotation myAnnotation = (MyAnnotation) annotation;
        //     System.out.println(myAnnotation.name());
        //     System.out.println(myAnnotation.value());
        // }

        // Field field = aClass.getField("someData");
        // annotations = field.getDeclaredAnnotations();

        // for (Annotation annotation2: annotations) {
        //     if (annotation2 instanceof MyAnnotation) {
        //         MyAnnotation myAnnotation = (MyAnnotation) annotation2;
        //         System.out.println(myAnnotation.name());
        //         System.out.println(myAnnotation.value());
        //     }
        //  }

        //  annotation = field.getAnnotation(MyAnnotation.class);
        //  if (annotation instanceof MyAnnotation) {
        //     MyAnnotation myAnnotation = (MyAnnotation) annotation;
        //     System.out.println(myAnnotation.name());
        //     System.out.println(myAnnotation.value());
        // }

        Class[] cArg = new Class[1];
        cArg[0] = String.class;

        Method method = aClass.getMethod("doSomething", cArg);
        Annotation[][] parameterAnnotations = method.getParameterAnnotations();
        Class[] parameterTypes = method.getParameterTypes();

        int i = 0;

        for (Annotation[] annotation3 : parameterAnnotations) {
            Class parameterType = parameterTypes[i++];

            for (Annotation annot: annotation3) {
                if (annot instanceof MyAnnotation) {
                    MyAnnotation myAnnotation = (MyAnnotation) annot;
                    System.out.println("Param:" + parameterType.getName());
                    System.out.println("Name:" + myAnnotation.name());;
                    System.out.println("value:" + myAnnotation.value());;
                }
            }

        }

    }
}
