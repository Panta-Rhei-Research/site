---
{
  "projection_kind": "taulib_declaration",
  "title": "first_bombshell",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/first-bombshell/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::first_bombshell",
  "declaration_slug": "first-bombshell",
  "kind": "theorem",
  "name": "first_bombshell",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 547,
  "source_line_end": 555,
  "registry_ids": [
    "VII.L13"
  ],
  "related_registry_items": [
    {
      "id": "VII.L13",
      "title": "First Bombshell Lemma",
      "url": "/registry/object/VII.L13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L547-L555",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L547-L555",
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
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L547-L555)
- Source range: L547-L555
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.L13` — First Bombshell Lemma

## Immediate Comment / Docstring

```lean
/-- [VII.L13] First Bombshell (ch89). Three claims about "earning the language":
    (1) Circular foundations: taking ethical vocabulary as primitive is circular
    (2) Naturalistic fallacy: deriving from empirical facts commits is-ought gap
    (3) Earned vocabulary: in τ, Stages K+S show ethical vocabulary is constructed
        from self-enrichment at E₃. The is-ought gap dissolves because Reg_P
        exists alongside (not derived from) Reg_E.

    The practical register is as fundamental as the empirical register —
    both are readout functors on the same kernel. -/
```

## Source Excerpt

```lean
theorem first_bombshell :
    -- Practical register is fundamental
    reg_P.register_type = .practical ∧
    reg_P.action_guiding = true ∧
    -- Not derived from empirical register
    reg_E.register_type ≠ reg_P.register_type ∧
    -- Both emerge from kernel
    kernel_result.from_saturation = true :=
  ⟨rfl, rfl, by decide, rfl⟩
```
