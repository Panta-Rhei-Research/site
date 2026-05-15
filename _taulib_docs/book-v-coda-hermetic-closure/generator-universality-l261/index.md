---
{
  "projection_kind": "taulib_declaration",
  "title": "generator_universality",
  "permalink": "/corpus/taulib/docs/book-v-coda-hermetic-closure/generator-universality-l261/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Coda.HermeticClosure`.",
  "declaration_id": "TauLib.BookV.Coda.HermeticClosure::generator_universality",
  "declaration_slug": "generator-universality-l261",
  "kind": "theorem",
  "name": "generator_universality",
  "module_name": "TauLib.BookV.Coda.HermeticClosure",
  "module_url": "/corpus/taulib/docs/book-v-coda-hermetic-closure/",
  "source_line_start": 261,
  "source_line_end": 265,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L261-L265",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.HermeticClosure",
        "url": "/corpus/taulib/docs/book-v-coda-hermetic-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L261-L265",
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

- Module: [TauLib.BookV.Coda.HermeticClosure](/corpus/taulib/docs/book-v-coda-hermetic-closure/)
- Source path: [`TauLib/BookV/Coda/HermeticClosure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L261-L265)
- Source range: L261-L265
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Generator universality: 5 generators, no RG flow, depth-dependent coupling. -/
```

## Source Excerpt

```lean
theorem generator_universality :
    gen_universality.n_generators = 5 ∧
    gen_universality.no_rg_flow = true ∧
    gen_universality.depth_dependent = true :=
  ⟨rfl, rfl, rfl⟩
```
