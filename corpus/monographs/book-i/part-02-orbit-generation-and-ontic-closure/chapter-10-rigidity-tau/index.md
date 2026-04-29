---
layout: "corpus-monograph-chapter"
title: "Chapter 9: Rigidity — (τ) = \\\\"
permalink: "/corpus/monographs/book-i/part-02-orbit-generation-and-ontic-closure/chapter-10-rigidity-tau/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "I"
book_slug: "book-i"
part_number: 2
part_display: "Part II"
part_slug: "part-02-orbit-generation-and-ontic-closure"
chapter_number: 10
chapter_slug: "chapter-10-rigidity-tau"
page_in_book: 37
prev_chapter_url: "/corpus/monographs/book-i/part-02-orbit-generation-and-ontic-closure/chapter-09-the-iterator-of-iterator-ladder-and-tetration-saturation/"
prev_chapter_title: "Chapter 9: The Iterator-of-Iterator Ladder and Tetration Saturation"
next_chapter_url: "/corpus/monographs/book-i/part-03-the-denotational-bridge/chapter-10-tau-idx-the-alpha-orbit-as-internal-natural-numbers/"
next_chapter_title: "Chapter 10: τ-Idx — The Alpha-Orbit as Internal Natural Numbers"
summary_short: "Aut(τ) = {id} and τ₀ is categorical: every automorphism is the identity and any two models of the six kernel axioms are uniquely isomorphic, completing Part II's ontic seal."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-02-orbit-generation-and-ontic-closure/"
canonical_part_title: "Orbit Generation and Ontic Closure"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-02-orbit-generation-and-ontic-closure/chapter-10-rigidity-tau/"
right_rail:
  related:
    -
      title: "Book I: Categorical Foundations"
      url: "/corpus/monographs/book-i/"
    -
      title: "Part II: Orbit Generation and Ontic Closure"
      url: "/corpus/monographs/book-i/part-02-orbit-generation-and-ontic-closure/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-i/"
    -
      title: "Registry"
      url: "/registry/books/book-i/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book I"
    part: "Part II"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 3
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-01"
  - "CS-02"
---

The Ontic Closure Theorem (Chapter 8) established that Obj(τ) is ontically sealed: five pairwise disjoint sets, countable, with unique representation. This chapter adds the two culminating theorems that close Part II and make the seal absolute. The Rigidity Theorem (*I.T07*, registry *thm:rigidity*) proves that τ admits no non-trivial automorphisms: Aut(τ) = {id}. Every element of τ is uniquely determined by its structural position — its seed generator and its depth — not by the symbol used to name it. The Categoricity Theorem (*I.T08*, registry *thm:categoricity*) proves that τ₀ is categorical: any two structures satisfying K1–K6 are isomorphic via a unique isomorphism. Together, these results establish that τ is not merely *a* model of τ₀ but *the* model. No gauge freedom exists at the ontic level; what arrives in Part III is a rigid, unique, countable universe ready to receive arithmetic structure.

## What this chapter contributes

Two registry theorems are proved. For Rigidity (*I.T07*), the proof proceeds in four steps. Step 1: any Σ_τ-automorphism φ must fix ω (named constant in the signature). Step 2: φ must fix each of α, π, γ, η for the same reason. Step 3: for any orbit element x = ρⁿ(g), commutativity of φ with ρ and fixity of g gives φ(x) = φ(ρⁿ(g)) = ρⁿ(φ(g)) = ρⁿ(g) = x, by induction on n. Step 4: every element of Obj(τ) is covered, so φ = id. The proof is tight because it requires no lemmas beyond the Ontic Closure Theorem and the generator-fixity of constants.

For Categoricity (*I.T08*), the unique isomorphism φ: τ → M (for any model M ⊨ τ₀) is defined by φ(ω) := ω^M and φ(ρⁿ(g)) := (ρ^M)ⁿ(g^M). Well-definedness uses unique representation from *I.T01*; surjectivity uses K6 in M; injectivity uses pairwise disjointness in M (which follows from the same proof as *I.P03*, since that proof uses only K1–K6); uniqueness follows because any isomorphism must satisfy the same recurrence. A corollary records Label-Independence: any relabeling of the five generators that preserves K1 and the role assignments produces a uniquely isomorphic structure, confirming that the 2nd Edition's notation changes (γ, η replacing older symbols) carry no mathematical content.

A remark clarifies the relationship to first-order logic: K6 acts as a second-order closure axiom in spirit, eliminating non-standard models in the same way the second-order induction axiom makes Peano Arithmetic categorical. In the Lean formalization this issue does not arise because `TauObj` is defined inductively.

## Lean coverage

Formalized in `TauLib.BookI.Orbit.Rigidity`. Key items: `TauAutomorphism` defines the automorphism type; `auto_omega_to_omega` proves fixity of ω; `rigidity_non_omega` proves fixity of all ρⁿ(g) elements for *I.T07*; `TauModel` defines a model of τ-axioms on an arbitrary type; `categoricity_non_omega` proves the unique isomorphism for *I.T08*. All proofs compile without `sorry` (Lean 4, zero unproved goals).

## Where this leads

Part II is now complete. The four pillars — existence (Chapter 7), closure (Chapter 8), ladder structure (Chapter 9), and rigidity (this chapter) — collectively constitute the ontic foundation of the series. Part III crosses the ontic/denotational boundary: the same fixed, rigid, countable objects will now be named and addressed, receiving arithmetic (τ-Idx as internal natural numbers), coordinates (the ABCD chart), and eventually the full algebraic overlay that Books II–VII build upon.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part02/ch09-rigidity-categoricity.tex -->
