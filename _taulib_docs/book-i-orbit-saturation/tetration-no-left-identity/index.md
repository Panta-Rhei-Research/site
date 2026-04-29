---
{
  "projection_kind": "taulib_declaration",
  "title": "tetration_no_left_identity",
  "permalink": "/verify/taulib/docs/book-i-orbit-saturation/tetration-no-left-identity/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Saturation`.",
  "declaration_id": "TauLib.BookI.Orbit.Saturation::tetration_no_left_identity",
  "declaration_slug": "tetration-no-left-identity",
  "kind": "theorem",
  "name": "tetration_no_left_identity",
  "module_name": "TauLib.BookI.Orbit.Saturation",
  "module_url": "/verify/taulib/docs/book-i-orbit-saturation/",
  "source_line_start": 57,
  "source_line_end": 67,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L57-L67",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Saturation",
        "url": "/verify/taulib/docs/book-i-orbit-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L57-L67",
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

- Module: [TauLib.BookI.Orbit.Saturation](/verify/taulib/docs/book-i-orbit-saturation/)
- Source path: [`TauLib/BookI/Orbit/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L57-L67)
- Source range: L57-L67
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Tetration has no universal right identity.
    Proof: for e = 0, n↑↑0 = 1 ≠ n for n ≥ 2.
    For e = 1, n↑↑1 = n (works). But this is the only candidate,
    and for e ≥ 2, 2↑↑e ≥ 4 > 2, so e=1 is unique and we need to
    show there's no *other* candidate. Actually, e=1 IS a right identity.
    The claim should be: tetration has no right identity *other than 1*
    that works universally, AND the operation has no left identity.

    More precisely: there is no left identity for tetration.
    For any e, e↑↑n = n fails: e↑↑2 = e^e ≠ 2 for e ≥ 2. -/
```

## Source Excerpt

```lean
theorem tetration_no_left_identity :
    ¬∃ e, e ≥ 2 ∧ ∀ n, n ≥ 1 → tetration e n = n := by
  intro ⟨e, he, h⟩
  have h2 := h 2 (by omega)
  -- e↑↑2 = e^e. For e ≥ 2, e^e ≥ 4 > 2.
  simp [tetration] at h2
  -- h2: e ^ e = 2. But e ≥ 2 gives e^e ≥ 4.
  have h1 : (2 : Nat) ^ 2 ≤ e ^ 2 := Nat.pow_le_pow_left he 2
  have h2 : e ^ 2 ≤ e ^ e := Nat.pow_le_pow_right (by omega : e > 0) he
  have : e ^ e ≥ 2 ^ 2 := Nat.le_trans h1 h2
  omega
```
