---
{
  "projection_kind": "taulib_declaration",
  "title": "gen_distinct",
  "permalink": "/corpus/taulib/docs/book-i-kernel-axioms/gen-distinct/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Kernel.Axioms`.",
  "declaration_id": "TauLib.BookI.Kernel.Axioms::gen_distinct",
  "declaration_slug": "gen-distinct",
  "kind": "theorem",
  "name": "gen_distinct",
  "module_name": "TauLib.BookI.Kernel.Axioms",
  "module_url": "/corpus/taulib/docs/book-i-kernel-axioms/",
  "source_line_start": 142,
  "source_line_end": 146,
  "registry_ids": [
    "I.P01"
  ],
  "related_registry_items": [
    {
      "id": "I.P01",
      "title": "Generator Distinctness",
      "url": "/registry/object/I.P01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L142-L146",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.Axioms",
        "url": "/corpus/taulib/docs/book-i-kernel-axioms/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L142-L146",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.Kernel.Axioms](/corpus/taulib/docs/book-i-kernel-axioms/)
- Source path: [`TauLib/BookI/Kernel/Axioms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L142-L146)
- Source range: L142-L146
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `I.P01` — Generator Distinctness

## Immediate Comment / Docstring

```lean
/-- [I.P01] Generator distinctness: all five generators are pairwise distinct. -/
```

## Source Excerpt

```lean
theorem gen_distinct : ∀ (a b : Generator), a ≠ b → a.toNat ≠ b.toNat := by
  intro a b hab
  intro heq
  apply hab
  cases a <;> cases b <;> simp [Generator.toNat] at heq <;> try rfl
```
