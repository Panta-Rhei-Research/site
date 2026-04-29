---
{
  "projection_kind": "taulib_declaration",
  "title": "llm_subsymbolic_evidence",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/llm-subsymbolic-evidence/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::llm_subsymbolic_evidence",
  "declaration_slug": "llm-subsymbolic-evidence",
  "kind": "theorem",
  "name": "llm_subsymbolic_evidence",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 751,
  "source_line_end": 755,
  "registry_ids": [
    "VII.P14"
  ],
  "related_registry_items": [
    {
      "id": "VII.P14",
      "title": "LLM as Subsymbolic Evidence",
      "url": "/registry/object/VII.P14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L751-L755",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/verify/taulib/docs/book-vii-meta-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L751-L755",
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

- Module: [TauLib.BookVII.Meta.Saturation](/verify/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L751-L755)
- Source range: L751-L755
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.P14` — LLM as Subsymbolic Evidence

## Immediate Comment / Docstring

```lean
/-- [VII.P14] LLM as Subsymbolic Evidence (ch64). LLMs validate
    the subsymbolic layer claim: sophisticated language behaviour
    without symbolic rule manipulation. This is empirical evidence
    (Reg_E) for the subsymbolic layer (VII.D52). -/
```

## Source Excerpt

```lean
theorem llm_subsymbolic_evidence :
    para_mind.subsymbolic = true ∧
    para_mind.e2_level = true ∧
    para_mind.pattern_without_self_model = true :=
  ⟨rfl, rfl, rfl⟩
```
