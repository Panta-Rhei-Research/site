---
{
  "projection_kind": "taulib_declaration",
  "title": "mul_injective",
  "permalink": "/corpus/taulib/docs/book-i-orbit-ladder/mul-injective/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Ladder`.",
  "declaration_id": "TauLib.BookI.Orbit.Ladder::mul_injective",
  "declaration_slug": "mul-injective",
  "kind": "theorem",
  "name": "mul_injective",
  "module_name": "TauLib.BookI.Orbit.Ladder",
  "module_url": "/corpus/taulib/docs/book-i-orbit-ladder/",
  "source_line_start": 85,
  "source_line_end": 103,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L85-L103",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Ladder",
        "url": "/corpus/taulib/docs/book-i-orbit-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L85-L103",
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

- Module: [TauLib.BookI.Orbit.Ladder](/corpus/taulib/docs/book-i-orbit-ladder/)
- Source path: [`TauLib/BookI/Orbit/Ladder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L85-L103)
- Source range: L85-L103
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Multiplication by n > 0 is injective in the second argument. -/
```

## Source Excerpt

```lean
theorem mul_injective (n : Nat) (hn : n > 0) : Function.Injective (n * ·) := by
  intro a b h
  induction a generalizing b with
  | zero =>
    have h' : n * 0 = n * b := h
    rw [Nat.mul_zero] at h'
    cases b with
    | zero => rfl
    | succ b => rw [Nat.mul_succ] at h'; omega
  | succ a ih =>
    have h' : n * (a + 1) = n * b := h
    cases b with
    | zero => rw [Nat.mul_zero, Nat.mul_succ] at h'; omega
    | succ b =>
      congr 1
      apply ih
      show n * a = n * b
      rw [Nat.mul_succ, Nat.mul_succ] at h'
      omega
```
