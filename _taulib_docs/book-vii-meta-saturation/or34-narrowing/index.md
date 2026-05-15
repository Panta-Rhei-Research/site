---
{
  "projection_kind": "taulib_declaration",
  "title": "or34_narrowing",
  "permalink": "/corpus/taulib/docs/book-vii-meta-saturation/or34-narrowing/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::or34_narrowing",
  "declaration_slug": "or34-narrowing",
  "kind": "theorem",
  "name": "or34_narrowing",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/corpus/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 501,
  "source_line_end": 504,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L501-L504",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/corpus/taulib/docs/book-vii-meta-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L501-L504",
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

- Module: [TauLib.BookVII.Meta.Saturation](/corpus/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L501-L504)
- Source range: L501-L504
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [VII.Lxx] OR3+OR4 Narrowing: diagonal-free + NF-addressable force
    NF-address structure compatible with self-description. This entails
    axioms K0–K4 (the combinatorial axioms governing the address space). -/
```

## Source Excerpt

```lean
theorem or34_narrowing :
    six_requirements.or3_diagonal_free = true ∧
    six_requirements.or4_nf_addressable = true :=
  ⟨rfl, rfl⟩
```
