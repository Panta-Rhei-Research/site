---
{
  "projection_kind": "taulib_declaration",
  "title": "alethic_pluralism",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/alethic-pluralism/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::alethic_pluralism",
  "declaration_slug": "alethic-pluralism",
  "kind": "theorem",
  "name": "alethic_pluralism",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 784,
  "source_line_end": 787,
  "registry_ids": [
    "VII.P16"
  ],
  "related_registry_items": [
    {
      "id": "VII.P16",
      "title": "Alethic Pluralism",
      "url": "/registry/object/VII.P16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L784-L787",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L784-L787",
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
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L784-L787)
- Source range: L784-L787
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.P16` — Alethic Pluralism

## Immediate Comment / Docstring

```lean
/-- [VII.P16] Alethic Pluralism (ch42). Different registers employ
    different truth-maker levels: Reg_E uses inclusion (empirical
    verification), Reg_D uses diagram (formal proof), Reg_C uses
    invariant (stance-stability). This is structural pluralism,
    not relativism. -/
```

## Source Excerpt

```lean
theorem alethic_pluralism :
    truth_maker_logical.level_count = 4 ∧
    truth_bearer.bearer_as_section = true :=
  ⟨rfl, rfl⟩
```
