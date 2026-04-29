---
{
  "projection_kind": "taulib_declaration",
  "title": "DutyTyping",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/duty-typing/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::DutyTyping",
  "declaration_slug": "duty-typing",
  "kind": "structure",
  "name": "DutyTyping",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 185,
  "source_line_end": 196,
  "registry_ids": [
    "VII.L11"
  ],
  "related_registry_items": [
    {
      "id": "VII.L11",
      "title": "Duty Typing Lemma",
      "url": "/registry/object/VII.L11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L185-L196",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L185-L196",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L185-L196)
- Source range: L185-L196
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.L11` — Duty Typing Lemma

## Immediate Comment / Docstring

```lean
/-- [VII.L11] Duty Typing Lemma (ch78). An obligation D is properly typed iff:
    (1) Local realizability: D(U) ≠ ∅ for every perspective U
    (2) Dignity preservation: every enactment factors through L_dig
    (3) Overlap compatibility: restriction maps agree on pairwise overlaps
    (4) Bounded tension: no enactment forces unbounded tension

    Properly typed iff D is a subsheaf of Max. -/
```

## Source Excerpt

```lean
structure DutyTyping where
  /-- (1) Local realizability. -/
  local_realizable : Bool := true
  /-- (2) Dignity preservation. -/
  dignity_preserving : Bool := true
  /-- (3) Overlap compatibility. -/
  overlap_compatible : Bool := true
  /-- (4) Bounded tension. -/
  bounded_tension : Bool := true
  /-- All conditions = subsheaf of Max. -/
  is_subsheaf : Bool := true
  deriving Repr
```
