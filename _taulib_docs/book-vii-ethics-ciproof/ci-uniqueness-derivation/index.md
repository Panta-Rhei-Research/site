---
{
  "projection_kind": "taulib_declaration",
  "title": "ci_uniqueness_derivation",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/ci-uniqueness-derivation/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::ci_uniqueness_derivation",
  "declaration_slug": "ci-uniqueness-derivation",
  "kind": "theorem",
  "name": "ci_uniqueness_derivation",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 520,
  "source_line_end": 532,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L520-L532",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L520-L532",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L520-L532)
- Source range: L520-L532
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [VII.Lxx] CI Uniqueness Derivation: the full chain from lattice
    completeness through Knaster-Tarski to uniqueness. -/
```

## Source Excerpt

```lean
theorem ci_uniqueness_derivation :
    -- Lattice structure
    f_lattice.complete_lattice = true ∧
    f_lattice.intersection_closed = true ∧
    -- Non-emptiness from Kernel Theorem
    kernel_result.existence = true ∧
    f_lattice.non_empty = true ∧
    -- Uniqueness of minimum
    f_lattice.has_unique_minimum = true ∧
    -- CI is that minimum
    ci_graph.minimal = true ∧
    ci_graph.j_closed = true :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
```
